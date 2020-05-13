#!/bin/sh

file=$(echo $2 | sed 's/ /_/g')

elinks -dump 1 $1 -dump-width 90 -no-references -no-numbering > $file
echo $1 >> $file
txt2otl.sh $file && rm -f $file
