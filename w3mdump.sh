#!/bin/bash

file=$(echo $2 | sed 's/ /_/g')

w3m -dump $1 -cols 90 > $file
echo $1 >> $file
txt2otl.sh $file && rm -f $file
