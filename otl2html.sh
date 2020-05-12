#!/bin/bash

function gvim_otl2html()
{
	gvim -U ~/.gvimrc-otl-white -c ':set foldlevel=9999999999' -c ':TOhtml' \
	-c ':wa!' -c ':quitall' $1
}

if [ $# -eq 0 ]
then
	for i in *.otl
	do
		gvim_otl2html $i
	done
else
	until [ -z "$1" ]
	do
		gvim_otl2html $1
		shift
	done
fi
