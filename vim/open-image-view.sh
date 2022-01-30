#!/bin/bash

# vrdel
# dependency: feh

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
	img=${args#*(}
	img=${img%)}
fi

feh --scale-down $img &
