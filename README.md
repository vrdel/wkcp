# Wkcp

**Wkcp** is a command-line helper tool designed to manage text, image attachments, and links within Markdown and Vimwiki files.

It simplifies the handling of remote and local images by providing tools to:
- Download images from remote URLs referenced in Markdown and Vimwiki files.
- Place downloaded images in the same directory as the document.
- Convert remote URLs to local Markdown or Vimwiki links referencing the newly saved local image.
- Copy image content or image paths directly to the system clipboard from a local link.
- Paste images from the clipboard right into a document's directory with an auto-generated filename and automatically build the corresponding link.
- Copy or delete wikis and their referenced local images elegantly.

## Installation and Execution

The project uses Poetry/Setuptools for dependency management.

There is also a provided `docker-run-wkcp.py` script which acts as a wrapper for running `wkcp` inside a Docker container. It automatically mounts directories of any absolute file paths passed as arguments and passes through the X11 socket (allowing clipboard access with `copykitten` via Docker) while using the host network.

## CLI Usage and Subcommands

`wkcp [command] [options]`

### `image` (Handle Image Links and CLI Clipboard Integration)
Extract, transform, copy, paste, or delete images.
- `--copypath`: Copy extracted image path to the clipboard.
- `--pastepath`: Copy an image file to the current folder of the wiki file and build an image link.
- `--pasteimg`: Dump image from the clipboard directly to the document's folder with a generated filename and build the link.
- `--deleteimg`: Delete the image file.
- `-w`: Build a Vimwiki formatted image link.
- `-m`: Build a Markdown formatted image link.
- `-mw`: Build a Markdown formatted wikilink for the image.
- `--copyimg`: Read image content and copy it to the clipboard.
- `--link`: A list of image paths that will be extracted, transformed, and copied to the clipboard.

### `download` (Download Remote Attachments)
Automates the downloading and local linking of remote images inside a markdown or vimwiki file.
- `--file <path>`: Required path to the file containing attachments that will be downloaded and replaced with local file references.
- `-w`: Re-build as Vimwiki image links.
- `-m`: Re-build as Markdown image links.
- `-mw`: Re-build as Markdown image wikilinks.

### `filename` (Generate Dynamic Filenames)
Utility to generate filenames automatically, useful for attachments.
- `--prefix <string>`: Prepend a custom prefix.
- `--suffix <string>`: Append a custom suffix.
- `--snake-case`: Format prefix/suffix as `snake_case`.
- `--kebab-case`: Format prefix/suffix as `kebab-case`.
- `--lower`: Convert the prefix/suffix to lowercase.
- `--clipboard`: Copy the newly generated filename directly to the clipboard.
- `--path <path>`: File path whose extension will be extracted and used in the generated filename.

### `copywiki` (Copy and Convert Wiki Files)
Copy a Vimwiki/Markdown file along with all referenced local images to a destination folder. Includes options to instantly convert the document format using Pandoc.
- `--file <path>`: Path to the source markdown/vimwiki file.
- `--dest <dir>`: Destination folder.
- `--convert-md`: Convert the source file to Markdown using Pandoc.
- `--convert-vimwiki`: Convert the source file to Vimwiki using Pandoc.

### `deletewiki` (Delete Wiki Files)
Delete a Vimwiki/Markdown file and all the local images it references from the disk.
- `--file <path>`: Path to the markdown/vimwiki file.
