#!/bin/bash

# vrdel
# dependency: feh

IFS=''
args=''

for a in $*
do
	args="$args$a"
done

if echo $args | grep -q 'myimg:'
then
	img=${args#*myimg:}
	img=${img%%\}*}
elif echo $args | egrep -q 'img.?='
then
	img=${args#*img*=}
	img=${img# *}
elif echo $args | grep -q '(.*)'
then
	if echo $args | grep -q '%20'
	then
		args=${args//%20/ }""
	fi
	if echo $args | grep -q '%'
	then
		args=${args//%/\\x}""
	fi
	img=${args#*(}
	img=${img%)}
	img=${img%\)\'}
elif echo $args | grep -q '\[\[.*\]\]'
then
	img=${args#*\[\[}
	img=${img%\]\]*}
fi

if echo $img | grep -q '.otl.png'
then
	img=${img/.otl/}
fi

if echo $img | grep -q '.mmd.png'
then
	img=${img/.mmd/}
fi

if echo $img | grep -q "^/"
then
	feh --scale-down "$img" &
else
	feh --scale-down "$PWD/$img" &
fi
