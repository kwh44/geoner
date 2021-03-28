#!/bin/bash

docker run -ti --name geoner --mount type=bind,source=/data/geoner,target=/home/geoner \
    --privileged \
    -p 8888:8888 \
    --volume=/tmp/.X11-unix:/tmp/.X11-unix \
    --device=/dev/dri:/dev/dri \
    --env="DISPLAY=$DISPLAY" \
    --env QT_X11_NO_MITSHM=1 \
	  kwh44/geoner:latest bash
