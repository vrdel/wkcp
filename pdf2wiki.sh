#!/bin/sh

pdftotext -nopgbrk -layout "$1"
mv "${1%.*}".txt "${1%.*}".wiki
echo 'vim: tw=0 ft=vimwiki' >> "${1%.*}".wiki
