#!/bin/bash

# vrdel
# dependency: elinksdump.sh, xclip

joined=''

while read line
do
	line=$(echo $line | sed 's/#//g' | tr -d '\n')
	joined="$joined$line"
done

joined=$(echo -n $joined | sed 's/[ ]*//g')
echo $joined
