#!/bin/bash

# vrdel
# dependency: elinksdump.sh, xclip

dir=$(dirname "$1")
file=$(basename "$1")

if [ -n "$dir" ];
then
	cd $dir
	dir=$PWD
fi

echo -n "$dir"/"$file" | xclip -i -selection clipboard
