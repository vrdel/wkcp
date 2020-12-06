#!/bin/bash

# vrdel

file=$(xclip -o -selection clipboard)

cp -f $file .

str="![$(basename $file)]($(basename $file))"

echo $str
