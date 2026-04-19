import argparse
import sys

from wkcp.text import TextHandle
from wkcp.image import ImageHandle
from wkcp.download import DownloadHandle
from wkcp.copywiki import CopyWikiHandle
from wkcp.deletewiki import DeleteWikiHandle
from wkcp.extractembedded import ExtractEmbeddedHandle
from wkcp.utils import build_filename


def main():
    parser = argparse.ArgumentParser(description="wkcp - Copy/paste and handle text and image attachments from markdowns and vimwikis")
    subparsers = parser.add_subparsers(help="Subcommands", dest="command")
    parser_image = subparsers.add_parser("image", help="Handle images")
    # parser_text = subparsers.add_parser("text", help="Handle text")
    parser_download = subparsers.add_parser("download", help="Download attachments")
    parser_filename = subparsers.add_parser("filename", help="Generate filename")
    parser_copywiki = subparsers.add_parser("copywiki", help="Copy vimwiki/markdown file and all referenced local images to destination folder, optionally convert to vimwiki/markdown")
    parser_deletewiki = subparsers.add_parser("deletewiki", help="Delete vimwiki/markdown file and all referenced local images")
    parser_extractembedded = subparsers.add_parser("extract-embedded", help="Extract embedded base64 images from markdown file")

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
    parser_filename.add_argument("--suffix", dest="customsuffix", default=False,
                                 required=False, help="Build filename with custom suffix")
    parser_filename.add_argument("--snake-case", dest="snake_case", action="store_true",
                                 default=False, required=False, help="Format prefix/suffix as snake_case")
    parser_filename.add_argument("--kebab-case", dest="kebab_case", action="store_true",
                                 default=False, required=False, help="Format prefix/suffix as kebab-case")
    parser_filename.add_argument("--lower", dest="lower", action="store_true",
                                 default=False, required=False, help="Make prefix/suffix lowercase")
    parser_filename.add_argument("--clipboard", dest="clipboard", action="store_true",
                                 default=False, required=False, help="Copy generated filename to clipboard")
    parser_filename.add_argument("--path", dest="extpath", default=False,
                                 required=False, help="File path whose extension will be extracted")

    parser_copywiki.add_argument("--file", dest="file", required=True, help="Path to markdown/vimwiki file")
    parser_copywiki.add_argument("--dest", dest="dest", required=True, help="Destination folder")
    parser_copywiki.add_argument("--convert-md", dest="convert_md", action="store_true", help="Convert source to markdown using pandoc")
    parser_copywiki.add_argument("--convert-vimwiki", dest="convert_vimwiki", action="store_true", help="Convert source to vimwiki using pandoc")

    parser_deletewiki.add_argument("--file", dest="file", required=True, help="Path to markdown/vimwiki file")
    parser_extractembedded.add_argument("--file", dest="file", required=True, help="Path to markdown/vimwiki file")

    args = parser.parse_args()

    if args.command == "image":
        ImageHandle(args)

    elif args.command == "text":
        TextHandle(args)

    elif args.command == "download":
        DownloadHandle(args)

    elif args.command == "filename":
        generated_filename = build_filename(args.extpath, prefix=args.customprefix, suffix=args.customsuffix, microsec=False, snake_case=args.snake_case, kebab_case=args.kebab_case, lower=args.lower)
        if args.clipboard:
            import copykitten
            copykitten.copy(generated_filename)
        sys.stdout.write(generated_filename)

    elif args.command == "copywiki":
        CopyWikiHandle(args)

    elif args.command == "deletewiki":
        DeleteWikiHandle(args)

    elif args.command == "extract-embedded":
        ExtractEmbeddedHandle(args)
