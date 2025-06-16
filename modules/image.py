import os
import copykitten
import shutil

from datetime import datetime
from PIL import Image

from wkcp.utils import extract_imgpaths


def handle(args):
    preprocess_links = list()

    if args.wikilink:
        for link in args.wikilink:
            preprocess_links.append(
                link.strip("\\\'")
            )

    if args.copypath:
        image_path = extract_imgpaths(preprocess_links)
        if image_path:
            copykitten.copy(image_path)
    elif args.copyimg:
        image_path = extract_imgpaths(preprocess_links)
        for image in image_path.split("\n"):
            pil_image = Image.open(image)
            if pil_image.mode != "RGBA":
                pil_image = pil_image.convert("RGBA")
            pixels = pil_image.tobytes()
            copykitten.copy_image(pixels, pil_image.width, pil_image.height)
    elif args.pastepath:
        image_path = copykitten.paste()
        try:
            shutil.copy2(image_path, os.getcwd())
            if args.pastepathmarkdownwikilink:
                print("![[{0}]]".format(os.path.basename(image_path)))
            elif args.pastepathvimwiki:
                print("{{myimg:{0}}}".format(os.path.basename(image_path)))
            else:
                print("![{0}]({0})".format(os.path.basename(image_path)))
        except FileNotFoundError:
            pass
    elif args.pasteimg:
        try:
            pixels, width, height = copykitten.paste_image()
            image = Image.frombytes(mode="RGBA", size=(width, height), data=pixels)
            now = datetime.now()
            datetime_string = now.strftime("%y%m%d-%H%M%S")
            image_filename = f"wkcp-pi-{datetime_string}.png"
            image.save(image_filename)
            try:
                if args.pastepathmarkdownwikilink:
                    print("![[{0}]]".format(os.path.basename(image_filename)))
                elif args.pastepathvimwiki:
                    print("{{" + "myimg:{0}".format(os.path.basename(image_filename)) + "}}")
                else:
                    print("![{0}]({0})".format(os.path.basename(image_filename)))
            except FileNotFoundError:
                pass
        except copykitten.CopykittenError as exc:
            pass
    elif args.deleteimg:
        image_path = extract_imgpaths(preprocess_links)
        if image_path:
            try:
                os.remove(image_path)
                print("DELETED")
            except FileNotFoundError:
                pass
