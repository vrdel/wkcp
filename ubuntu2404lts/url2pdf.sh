#!/bin/bash

gpaste=$(which gpaste-client)

if (( $? > 0 ))
then
	gpaste=$(which gpaste)
fi

url=$($gpaste | head -n1 | awk '{print $2'})
filename=$(zenity --title "html2pdf" --entry --text="Page to be converted:\n\t$url\n\nEnter PDF filename:" --entry-text="$url" | sed 's/ /_/g')

if [ -n "$filename" ];
then
	# CutyCapt --smooth --url="$url" --out="$HOME/documents/Web2Pdf/""$filename.pdf" && \
	wkhtmltopdf -q -l "$url" "$HOME/documents/Web2Pdf/""$filename.pdf" | \
	zenity --progress --pulsate --text='Finished' --no-cancel
fi
