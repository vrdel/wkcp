import aiohttp
import asyncio

from aiohttp import client_exceptions
from pathlib import Path, PosixPath
from urllib.parse import urlparse

from wkcp.utils import extract_img, merge_dicts, contains_exception, build_image_filename
from wkcp.exceptions import DownloadError


class DownloadHandle:
    def __init__(self, args):
        self.args = args
        self.filelines = list()
        self.lines_with_images = list()
        self.image_links = list()
        self._run()

    def _read_file(self):
        with open(self.args.file[0], 'r') as fp:
            self.filelines = fp.readlines()

    def _write_content_file(self, content, filename):
        with open(filename, 'wb') as f:
            f.write(content)

    async def _coro_download_image(self, url):
        session = aiohttp.ClientSession()

        try:
            async with session.get(url) as response:
                parsed_url = urlparse(url)
                image_filename = build_image_filename(parsed_url.path)
                content = await response.content.read()
                if Path(self.args.file[0]).parent == PosixPath('.'):
                    self._write_content_file(content, image_filename)
                    print(f"Downloaded {url} to {image_filename}")
                else:
                    parent = Path(self.args.file[0]).parent
                    self._write_content_file(content, parent.joinpath(Path(image_filename)).as_posix())
                    print(f"Downloaded {url} to {parent.joinpath(Path(image_filename)).as_posix()}")
                return {url: image_filename}

        except (client_exceptions.ClientError,
                client_exceptions.ServerTimeoutError,
                asyncio.TimeoutError) as exc:
            errmsg = 'ERROR: ' + f'{repr(exc)}'
            raise DownloadError(errmsg)

        finally:
            await session.close()

    def _extract_image_links(self):
        for i in range(len(self.filelines)):
            image = extract_img(self.filelines[i])
            if image:
                parsed_url = urlparse(image)
                if not (parsed_url.scheme or parsed_url.netloc):
                    continue
                self.lines_with_images.append(i)
                self.image_links.append(image)

    async def _download(self):
        coros = list()
        for image_link in self.image_links:
            coros.append(self._coro_download_image(image_link))

        return await asyncio.gather(*coros, return_exceptions=True)

    def _replace_with_local_links(self, local_files):
        for ln in self.lines_with_images:
            if self.args.markdownwikilink:
                self.filelines[ln] = "![[{0}]]\n".format(local_files[extract_img(self.filelines[ln])])
            elif self.args.vimwiki:
                self.filelines[ln] = "{{" + "myimg:{0}".format(local_files[extract_img(self.filelines[ln])]) + "}}\n"
            else:
                self.filelines[ln] = "![{0}]({0})\n".format(local_files[extract_img(self.filelines[ln])])

        with open(self.args.file[0], 'w') as fp:
            fp.writelines(self.filelines)

    def _run(self):
        self._read_file()
        self._extract_image_links()

        local_files = asyncio.run(self._download())
        exc_raised, exc = contains_exception(local_files)
        if exc_raised:
            print("Fully or partially unsuccesfull download, exiting...")
            print(exc)
            raise SystemExit(1)

        local_files = merge_dicts(local_files)

        self._replace_with_local_links(local_files)
