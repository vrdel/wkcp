#!/bin/bash

# vrdel
# dependancy: GraphicsMagick (http://www.graphicsmagick.org/)

export IFS=""

for f in *.png
do
	echo "Converting ${f} to jpg..."
	gm convert "${f}" -quality 80 "${f%.*}".jpg && rm -f "${f}"
done
