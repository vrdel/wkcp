#!/bin/bash

mtime="-1"

if [ ! -z $1 ];
then
	mtime=$1
fi

cd ~/documents/
find . -type f -mtime $mtime | grep '.*otl$' | $PAGER
