#!/bin/bash

# vrdel

while getopts 'mo' OPTION
do
	case $OPTION in
		m) md=1 ;;
		o) otl=1 ;;
		h)
			printf "Usage: %s
              [-m generate md image placeholder]
              [-o generate otl image placeholder]
              file.md,otl\n" $(basename $0) >&2
			exit 2
			;;
	esac
done
shift "$(( $OPTIND - 1 ))"

file=$(xclip -o -selection clipboard)

if [ ! -z "$md" ]
then
	cp -f $file .
	str="![$(basename $file)]($(basename $file))"
	echo $str
fi

if [ ! -z "$otl" ]
then
	cp -f $file .
	str="myimg:$(basename $file)"
	echo -e "\t: $str"
fi
