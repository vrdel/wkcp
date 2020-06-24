#!/bin/bash

# vrdel
# dependency: elinksdump.sh, xclip

if [ -z "$1" ]
then
	url=$(xclip -o -selection clipboard)
else
	url="file://$1"
fi

filename=$(basename "$url" | sed 's/ /_/g')

if [ -n "$filename" ];
then
	elinksdump.sh "$url" "$HOME/documents/Web2Otl/""$filename"
fi
