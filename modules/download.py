import aiohttp
import asyncio

from wkcp.utils import extract_img, merge_dicts, contains_exception

from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


async def coro_download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError(f"Failed to download {url}: HTTP {response.status}")

            parsed_url = urlparse(url)
            path = parsed_url.path
            extension = Path(path).suffix.lower()

            now = datetime.now()
            datetime_string = now.strftime("%y%m%d-%H%M%S-%f")
            image_filename = f"wkcp-di-{datetime_string}{extension}"

            with open(image_filename, 'wb') as f:
                while True:
                    chunk = await response.content.read()
                    if not chunk:
                        break
                    f.write(chunk)
            print(f"Downloaded {url} to {image_filename}")
            return {url: image_filename}


async def coro_download_run(coros):
    return await asyncio.gather(*coros, return_exceptions=True)


class DownloadHandle:
    filelines = list()
    lines_with_images = list()
    image_links = list()

    def __init__(self, args):
        self.args = args
        self._run()

    def _read_file(self):
        with open(self.args.file[0], 'r') as fp:
            self.filelines = fp.readlines()

    def _extract_image_links(self):
        for i in range(len(self.filelines)):
            image = extract_img(self.filelines[i])
            if image:
                parsed_url = urlparse(image)
                if not (parsed_url.scheme or parsed_url.netloc):
                    continue
                self.lines_with_images.append(i)
                self.image_links.append(image)

    def _download(self):
        coros = list()
        for image_link in self.image_links:
            coros.append(coro_download_image(image_link))

        local_files = asyncio.run(
            coro_download_run(coros)
        )

        exc_raised, exc = contains_exception(local_files)
        if exc_raised:
            print(local_files)
            print("Fully or partially unsuccesfull download, exiting...")
            raise SystemExit(1)

        return local_files

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

        local_files = self._download()
        local_files = merge_dicts(local_files)

        self._replace_with_local_links(local_files)
