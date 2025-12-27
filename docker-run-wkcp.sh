#!/bin/bash

docker run \
	--net host \
	--rm -v "$(pwd):/work" -w "/work" \
	-t wkcp "$@"
