import re
import os

from datetime import datetime
from pathlib import Path, PosixPath

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


def build_image_filename(path, prefix=None, microsec=True):
    extension = Path(path).suffix.lower()
    now = datetime.now()
    if microsec:
        datetime_string = now.strftime("%y%m%d-%H%M%S-%f")
    else:
        datetime_string = now.strftime("%y%m%d-%H%M%S")
    if not prefix:
        return f"wkcp-di-{datetime_string}{extension}"
    else:
        return f"{prefix}-{datetime_string}{extension}"


def build_filename(path, prefix=None, microsec=True):
    extension = Path(path).suffix.lower()
    parent = Path(path).parent
    now = datetime.now()
    if microsec:
        datetime_string = now.strftime("%y%m%d-%H%M%S-%f")
    else:
        datetime_string = now.strftime("%y%m%d-%H%M%S")

    if not prefix:
        if parent != PosixPath('.'):
            return f"{str(parent)}/wkcp-di-{datetime_string}{extension}"
        else:
            return f"wkcp-di-{datetime_string}{extension}"
    else:
        if parent != PosixPath('.'):
            return f"{str(parent)}/{prefix}-{datetime_string}{extension}"
        else:
            return f"{prefix}-{datetime_string}{extension}"
