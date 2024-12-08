#!/bin/bash

# vrdel

while getopts 'hmowcv' OPTION
do
	case $OPTION in
		m) md=1 ;;
		o) otl=1 ;;
		w) wiki=1 ;;
		v) move=1 ;;
		c) montage=1 ;;
		h)
			printf "Usage: %s
              [-m generate md image placeholder]
              [-o generate otl image placeholder]
              [-w generate vimwiki image placeholder]
              [-c generate montage image placeholder]
              [-v move instead of copy img in folder]
              file.md,otl,wiki\n" $(basename $0) >&2
			exit 2
			;;
	esac
done
shift "$(( $OPTIND - 1 ))"

file=$(xclip -o -selection clipboard)
file=${file/user\//$(whoami)\/}

oper="cp"
if [ ! -z "$move" ]
then
	oper="mv"
fi

if [ ! -z "$md" ]
then
	${oper} -f $file . &> /dev/null
	str="![$(basename $file)]($(basename $file))"
	echo $str
fi

if [ ! -z "$otl" ]
then
	${oper} -f $file . &> /dev/null
	str="myimg:$(basename $file)"
	echo -e "\t: $str"
fi

if [ ! -z "$wiki" ]
then
	${oper} -f $file . &> /dev/null
	str="{{myimg:$(basename $file)}}"
	echo -e "$str"
fi

if [ ! -z "$montage" ]
then
	${oper} -f $file . &> /dev/null
	ext="${file##*.}"
	filename="${file%.*}"
	filename=$(echo $filename | sed 's/\.//g')
	str="$(basename ${filename}.${ext})"
	mv $(basename $file) $str
	echo -e "$str"
fi
