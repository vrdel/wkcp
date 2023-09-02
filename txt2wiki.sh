#!/bin/bash

cp ${1} "${1%.*}".wiki
sed -i -e "s/^/\t: /g" "${1%.*}".wiki
sed -i -e "s/•/*/g" "${1%.*}".wiki
echo ': vim: nowrap tw=0 ft=vimwiki foldmethod=syntax foldtext=VimwikiFoldText()' >> "${1%.*}".wiki
