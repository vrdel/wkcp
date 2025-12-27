#!/bin/bash

docker run \
	--net host \
	--rm -v "$(pwd):/work" -w "/work" \
	-e "DISPLAY=$DISPLAY" \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-t wkcp "$@"
