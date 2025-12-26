import aiohttp
import asyncio

from wkcp.utils import extract_img

from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def merge_dicts(dict_list):
    result = {}
    for d in dict_list:
        if d:
            key, value = next(iter(d.items()))
            result[key] = value
    return result


def contains_exception(list):
    for a in list:
        if isinstance(a, Exception):
            return (True, a)

    return (False, None)


def extract_image_links(filelines):
    lines_with_images = list()
    image_links = list()
    for i in range(len(filelines)):
        image = extract_img(filelines[i])
        if image:
            parsed_url = urlparse(image)
            if not (parsed_url.scheme or parsed_url.netloc):
                continue
            lines_with_images.append(i)
            image_links.append(image)

    return image_links, lines_with_images


async def download_image(url):
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


async def download_run(coros):
    return await asyncio.gather(*coros, return_exceptions=True)


def handle(args):
    filelines = list()

    with open(args.file[0], 'r') as fp:
        filelines = fp.readlines()

    image_links, lines_with_images = extract_image_links(filelines)

    coros = list()
    for image_link in image_links:
        coros.append(download_image(image_link))

    local_files = asyncio.run(download_run(coros))

    exc_raised, exc = contains_exception(local_files)
    if exc_raised:
        print(local_files)
        print("Fully or partially unsuccesfull download, exiting...")
        raise SystemExit(1)

    local_files = merge_dicts(local_files)

    for ln in lines_with_images:
        if args.markdownwikilink:
            filelines[ln] = "![[{0}]]\n".format(local_files[extract_img(filelines[ln])])
        elif args.vimwiki:
            filelines[ln] = "{{" + "myimg:{0}".format(local_files[extract_img(filelines[ln])]) + "}}\n"
        else:
            filelines[ln] = "![{0}]({0})\n".format(local_files[extract_img(filelines[ln])])

    with open(args.file[0], 'w') as fp:
        fp.writelines(filelines)
