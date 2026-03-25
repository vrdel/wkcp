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


def build_filename(path=None, prefix=None, suffix=None, microsec=True,
                   timestamp=False, snake_case=False, kebab_case=False,
                   lower=False):
    if path:
        extension = Path(path).suffix.lower()
        parent = Path(path).parent
    else:
        extension = ""
        parent = PosixPath('.')
    now = datetime.now()
    if microsec and timestamp:
        datetime_string = now.strftime("%y%m%d-%H%M%S-%f")
    elif timestamp:
        datetime_string = now.strftime("%y%m%d-%H%M%S")
    else:
        datetime_string = now.strftime("%y%m%d")

    def format_str(s):
        if snake_case:
            s = re.sub(r'\s+', '_', s)
            s = re.sub(r'[^a-zA-Z0-9_]', '', s)
        elif kebab_case:
            s = re.sub(r'\s+', '-', s)
            s = re.sub(r'[^a-zA-Z0-9\-]', '', s)
        if lower:
            s = s.lower()
        return s

    if prefix:
        prefix = format_str(prefix)

    if suffix:
        suffix = format_str(suffix)

    if prefix and suffix:
        file_name = f"{prefix}-{datetime_string}-{suffix}{extension}"
    elif prefix:
        file_name = f"{prefix}-{datetime_string}{extension}"
    elif suffix:
        file_name = f"{datetime_string}-{suffix}{extension}"

    if not (prefix or suffix):
        base_name = "wkcp-di"
        file_name = f"{base_name}-{datetime_string}{extension}"

    if parent != PosixPath('.'):
        return f"{str(parent)}/{file_name}"
    else:
        return file_name
