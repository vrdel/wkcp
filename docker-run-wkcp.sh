#!/bin/bash

filemount=''

for a in $*
do
	if $(test -f $a) && $(echo $a | egrep -q '^\/')
	then
		filemount="$a"
	fi
done

if $(test ! -z $filemount)
then
	docker run \
		--net host \
		--rm -v "$(pwd):/work" -w "/work" \
		-e "DISPLAY=$DISPLAY" \
		-v /tmp/.X11-unix:/tmp/.X11-unix \
		-v $(dirname $filemount):$(dirname $filemount):rw \
		-t wkcp "$@"
else
	docker run \
		--net host \
		--rm -v "$(pwd):/work" -w "/work" \
		-e "DISPLAY=$DISPLAY" \
		-v /tmp/.X11-unix:/tmp/.X11-unix \
		-t wkcp "$@"
fi
