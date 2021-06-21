#!/bin/bash

function gvim_otl2html()
{
	gvim -U ~/.gvimrc-otl-white -c ':set foldlevel=9999999999' -c ':TOhtml' \
	-c ':wa!' -c ':quitall' $1
}

while getopts 'id:ht:' OPTION
do
	case $OPTION in
		i) img=1 ;;
		d) doc="$OPTARG" ;;
		t) target="$OPTARG" ;;
		h)
			printf "Usage: %s
              [-i should process and copy images embedded into otl]
              [-d target otl]
              [-t copy img to specified directory]
              file.otl\n" $(basename $0) >&2
			exit 2
			;;
	esac
done
shift "$(( $OPTIND - 1 ))"

if [ ! -z "$doc" ]
then
	if [ -e "$doc".html ]
	then
		rm -f "$doc".html
	fi
	gvim_otl2html $doc
fi

if [ ! -z "$img" ]
then
	imgstrs=$(grep -o "myimg:.*" $doc)
	sleep 2
	echo $imgstrs | tr " " "\n" | while read img
	do
		targetimg=${img#"myimg:"}
		echo $targetimg
		cp -f $targetimg .
		cp -f $(basename $targetimg) $target/${PWD#*documents/}/
		searchstr="s/myimg:.*$(basename $targetimg)/<img src=$(basename $targetimg)>/g"
		cat "$doc".html | sed -r "$searchstr" > "$doc".html.1
		mv -f "$doc".html.1 "$doc".html
	done
fi
