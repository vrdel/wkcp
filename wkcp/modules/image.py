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
    return temp_ip


def handle(args, stdin_content):
    image_path = MARKDOWN_IMAGE_PATTERN.findall(stdin_content)
    if image_path:
        print(_prepend_path(image_path))
    else:
        image_path = WIKILINK_IMAGE_PATTERN.findall(stdin_content)
        if image_path:
            print(_prepend_path(image_path))
