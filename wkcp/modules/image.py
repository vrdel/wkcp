import re

MARKDOWN_IMAGE_PATTERN = re.compile(r'!\[.*?\]\((.*?)\)')
WIKILINK_IMAGE_PATTERN = re.compile(r'!\[\[(.*?)\]\]')

def handle(args, stdin_content):
    import ipdb; ipdb.set_trace()

    image_path = MARKDOWN_IMAGE_PATTERN.findall(stdin_content)
    if image_path:
        for path in image_path:
            print(path)
    else:
        image_path = WIKILINK_IMAGE_PATTERN.findall(stdin_content)
        if image_path:
            for path in image_path:
                print(path)
