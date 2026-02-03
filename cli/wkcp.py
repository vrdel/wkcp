import argparse
import sys

from wkcp.text import TextHandle
from wkcp.image import ImageHandle
from wkcp.download import DownloadHandle
from wkcp.utils import build_image_filename as build_filename


def main():
    parser = argparse.ArgumentParser(description="wkcp - Copy/paste and handle text and image attachments from markdowns and vimwikis")
    subparsers = parser.add_subparsers(help="Subcommands", dest="command")
    parser_image = subparsers.add_parser("image", help="Handle images")
    # parser_text = subparsers.add_parser("text", help="Handle text")
    parser_download = subparsers.add_parser("download", help="Download attachments")
    parser_filename = subparsers.add_parser("filename", help="Generate filename")

    parser_image.add_argument("--copypath", dest="copypath", default=False, action='store_true',
                              required=False, help="Copy extracted image path to clipboard")
    parser_image.add_argument("--pastepath", dest="pastepath", default=False, action='store_true',
                              required=False, help="Copy image to current folder of wiki file and build markdown link")
    parser_image.add_argument("--pasteimg", dest="pasteimg", default=False, action='store_true',
                              required=False, help="Dump image from clipboard to current folder of wiki file with generated filename and build link")
    parser_image.add_argument("--deleteimg", dest="deleteimg", default=False, action='store_true',
                              required=False, help="Delete image")
    parser_image.add_argument("-w", dest="pastepathvimwiki", default=False, action='store_true',
                              required=False, help="Build vimwiki image link")
    parser_image.add_argument("-m", dest="pastepathmarkdown", default=False, action='store_true',
                              required=False, help="Build markdown image link")
    parser_image.add_argument("-mw", dest="pastepathmarkdownwikilink", default=False, action='store_true',
                              required=False, help="Build markdown image wikilink")
    parser_image.add_argument("--copyimg", dest="copyimg", default=False, action='store_true',
                              required=False, help="Copy image content to clipboard")
    parser_image.add_argument("--link", dest="wikilink", nargs='+',
                              required=False, help="Image paths that will be extracted, transformed and copied to clipboard")

    # parser_text.add_argument("--copy", dest="copytext", type=bool, default=False,
    #                          required=False, help="Copy text to clipboard")

    parser_download.add_argument("--file", dest="file", nargs=1, required=True, help="""Path to file with
                                 attachments that will be downloaded and
                                 replaced with local attachs""")
    parser_download.add_argument("-w", dest="vimwiki", default=False,
                                 action='store_true', required=False,
                                 help="Build vimwiki image link")
    parser_download.add_argument("-m", dest="markdown", default=False,
                                 action='store_true', required=False,
                                 help="Build markdown image link")
    parser_download.add_argument("-mw", dest="markdownwikilink",
                                 default=False, action='store_true',
                                 required=False, help="Build markdown image wikilink")

    parser_filename.add_argument("--prefix", dest="customprefix", default=False,
                                 required=False, help="Build filename with custom prefix")
    parser_filename.add_argument("--path", dest="extpath", default=False,
                                 required=True, help="File path whose extension will be extracted")

    args = parser.parse_args()

    if args.command == "image":
        ImageHandle(args)

    elif args.command == "text":
        TextHandle(args)

    elif args.command == "download":
        DownloadHandle(args)

    elif args.command == "filename":
        sys.stdout.write(build_filename(args.extpath, args.customprefix, microsec=False))
