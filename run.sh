#!/bin/sh

image=$(basename $PWD)

docker run -d  --network=host -p 8080:8080  "${image}:latest"
