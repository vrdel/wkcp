#!/bin/bash

# vrdel
# dependency: feh

if echo $2 | grep -q 'myimg:'
then
	img=${2#*myimg:}
	img=${img%%\}*}
elif echo $2 | grep -q '(.*)'
then
	img=${2#*(}
	img=${img%)}
fi

feh --scale-down $img &
