import re

MARKDOWN_IMAGE_PATTERN = re.compile(r'!\[.*?\]\((.*?)\)')

def handle(args, stdin_content):
    image_path = MARKDOWN_IMAGE_PATTERN.findall(stdin_content)
    for path in image_path:
        print(path)
