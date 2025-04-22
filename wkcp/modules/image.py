import re
import os
import copykitten

MARKDOWN_IMAGE_PATTERN = re.compile(r'!\[.*?\]\((.*?)\)')
WIKILINK_IMAGE_PATTERN = re.compile(r'!\[\[(.*?)\]\]')

def handle(args, stdin_content):
    image_path = MARKDOWN_IMAGE_PATTERN.findall(stdin_content)
    if image_path:
        image_path = [f'{os.getcwd()}/{path}' for path in image_path]
        print(image_path)
    else:
        image_path = WIKILINK_IMAGE_PATTERN.findall(stdin_content)
        if image_path:
            image_path = [f'{os.getcwd()}/{path}' for path in image_path]
            print(image_path)
