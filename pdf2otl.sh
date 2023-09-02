#!/bin/bash

pdftotext -nopgbrk -layout "$1"
mv "${1%.*}".txt "${1%.*}".otl
sed -i -e "s/^/\t: /g" "${1%.*}".otl
echo ': vim: tw=0' >> "${1%.*}".otl
