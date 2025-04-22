import re
import os
import copykitten

MARKDOWN_IMAGE_PATTERN = re.compile(r'!\[.*?\]\((.*?)\)')
WIKILINK_IMAGE_PATTERN = re.compile(r'!\[\[(.*?)\]\]')


def _prepend_path(path_array):
    temp_ip = list()
    for path in path_array:
        if not path.startswith('/'):
            temp_ip.append(f'{os.getcwd()}/{path}')
        else:
            temp_ip.append(path)
    return '\n'.join(temp_ip)


def _extract_imgpaths(links):
    image_path = MARKDOWN_IMAGE_PATTERN.findall(''.join(links))
    if image_path:
        return _prepend_path(image_path)
    else:
        image_path = WIKILINK_IMAGE_PATTERN.findall(''.join(links))
        if image_path:
            return _prepend_path(image_path)

    return None


def handle(args):
    preprocess_links = list()

    for link in args.wikilink:
        preprocess_links.append(
            link.strip("\\\'")
        )

    if args.copypath:
        image_path = _extract_imgpaths(preprocess_links)
        if image_path:
            copykitten.copy(image_path)
