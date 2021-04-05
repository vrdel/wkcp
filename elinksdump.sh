#!/bin/sh

file=$(echo $2 | sed 's/ /_/g')

elinks -dump 1 "$1" -dump-width 90 -no-references -no-numbering > $file

let numlines=$(wc -l $file | awk '{print $1}')
if ((numlines <= 2))
then
	w3m -dump $1 >| $file
fi

echo "$1" >> $file
txt2otl.sh $file && rm -f $file
