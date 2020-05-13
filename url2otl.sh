#!/bin/bash

# vrdel
# dependency: elinksdump.sh, zenity, gpaste

gpaste=$(which gpaste-client)

if (( $? > 0 ))
then
	gpaste=$(which gpaste)
fi

if [ -n "$1" ]
then
	url=$1
else
	url=$($gpaste | head -n1 | awk '{print $2'})
fi

filename=$(zenity --title "url2otl" --entry --text="Page to be converted:\n\t$url\n\nEnter OTL filename:" | sed 's/ /_/g')

if [ -n "$filename" ];
then
	elinksdump.sh "$url" "$HOME/documents/Web2Otl/""$filename" | \
	zenity --progress --pulsate --text='Finished' --no-cancel
fi
