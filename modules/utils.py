import re
import os

MARKDOWN_IMAGE_PATTERN = re.compile(r'!\[.*?\]\((.*?)\)')
WIKILINK_IMAGE_PATTERN = re.compile(r'!\[\[(.*?)\]\]')
VIMWIKI_IMAGE_PATTERN = re.compile(r'\{\{myimg:(.*?)\}\}')


def _prepend_path(path_array):
    temp_ip = list()
    for path in path_array:
        if not path.startswith('/'):
            temp_ip.append(f'{os.getcwd()}/{path}')
        else:
            temp_ip.append(path)
    return '\n'.join(temp_ip)


def extract_imgpaths(links, path=True):
    image_path = MARKDOWN_IMAGE_PATTERN.findall(''.join(links))
    if image_path:
        if path:
            return _prepend_path(image_path)
        else:
            return '\n'.join(image_path)
    else:
        image_path = WIKILINK_IMAGE_PATTERN.findall(''.join(links))
        if image_path:
            if path:
                return _prepend_path(image_path)
            else:
                return '\n'.join(image_path)
        else:
            image_path = VIMWIKI_IMAGE_PATTERN.findall(''.join(links))
            if image_path:
                if path:
                    return _prepend_path(image_path)
                else:
                    return '\n'.join(image_path)

    return None


def extract_img(links):
    return extract_imgpaths(links, path=False)
