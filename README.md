# wkcp

Helper tool to manage Markdown and Vimwiki image attachment and links. It downloads images from remote URLs referenced in Markdown and Vimwiki files, place images in same directory where file resides and converts remote URL to local Markdown/Vimwiki link referencing local image. Additionally it can copy image to clipboard from local Markdown/Vimwiki link or paste the image from clipboard with auto-generated filename and Markdown/Vimwiki local link.

## dockerized installation

```
cd wkcp-source/
make clean && make wheel-devel
docker build --no-cache . -f Dockerfile -t wkcp
cp docker-run-wkcp.py ~/.bin/wkcp.py
```
