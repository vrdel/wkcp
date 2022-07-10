#!/bin/bash

# vrdel
# dependency: elinksdump.sh, zenity, xclip

if [ -n "$1" ]
then
	url=$1
else
	url=$(xclip -o -selection clipboard)
fi

filename=$(zenity --title "url2otl" --entry --text="Page to be converted:\n\t$url\n\nEnter OTL filename:" | sed 's/ /_/g')

if [ -n "$filename" ];
then
	elinksdump.sh "$url" "$HOME/documents/Web2Wiki/""$filename" -w | \
	zenity --progress --pulsate --text='Finished' --no-cancel
fi
