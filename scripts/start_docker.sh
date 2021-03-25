#!/bin/bash

docker run -ti --name geoner --mount type=bind,source=/data/geoner,target=/home/geoner kwh44/geoner:latest bash
