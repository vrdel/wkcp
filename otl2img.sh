#!/bin/bash

# vrdel
# dependancy: wkhtmltox (https://wkhtmltopdf.org/downloads.html)

CURDIR=$(pwd)
size=
notitle=
gvim=
png=0

while getopts 'gs:nhp' OPTION
do
	case $OPTION in
		s) size="$OPTARG" ;;
		g) gvim=1 ;;
		n) notitle=1 ;;
		p) png=1 ;;
		h)
			printf "Usage: %s [-g run inside gvim with already converted html]
                  [-n no title]
                  [-p png output]
                  [-s 800+arg] file.otl\n" $(basename $0) >&2
			exit 2
			;;
	esac
done
shift "$(( $OPTIND - 1 ))"

if [ -z "$size" ]
then
	size=800
else
	size=$((800 + ${size}))
fi

if [ "$png" -eq 1 ]
then
	ext="png"
else
	ext="jpg"
fi

if [ -z "$gvim" ]
then
	gvim -f -U ~/.gvimrc-otl-white -c ':set foldlevel=999999' -c ':TOhtml' \
	-c ':wa!' -c ':quitall' "${PWD}/${1}" && \
	wkhtmltoimage --quality 100 file:///"${CURDIR}/${1}.html" "${1%.*}".$ext
	rm -f "${CURDIR}/${1}.html"
else
	wkhtmltoimage --quality 100 file:///"${CURDIR}/${1}.html" "${1%.*}".$ext
	rm -f "${CURDIR}/${1}.html"
fi

if [ "$notitle" ]
then
	galaview.sh "${1%.*}".$ext
else
	montit.py -s xs -t "${1%.*}" "${PWD}/${1%.*}".$ext "${PWD}/${1%.*}".$ext
	galaview.sh "${1%.*}".$ext
fi
