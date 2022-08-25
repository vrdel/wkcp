#!/bin/sh

pdftotext -nopgbrk -layout "$1"
mv "${1%.*}".txt "${1%.*}".wiki
sed -i -e "s/•/*/g" "${1%.*}".wiki
echo 'vim: tw=0 ft=vimwiki foldmethod=syntax foldtext=VimwikiFoldText()' >> "${1%.*}".wiki
