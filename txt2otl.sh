#!/bin/bash

cp ${1} "${1%.*}".otl
sed -i -e "s/^/\t: /g" "${1%.*}".otl
echo ': vim: nowrap tw=0' >> "${1%.*}".otl
