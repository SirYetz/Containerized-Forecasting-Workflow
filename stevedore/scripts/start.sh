#!/bin/bash
#Simple script to start the built stevedore image in docker
#Volume mount to .Xauthority and .X11-unix allow GUI applications to be displayed in host
#Volume mount from /opt/Containerized-Forecasting-Workflow allow for changes to scripts to be made from the host rather than within the container

docker run -w /opt/deepthunder --net=host -e DISPLAY -e DEEPTHUNDER_ROOT=/opt/deepthunder -v /data:/opt/deepthunder/data -v /opt/Containerized-Forecasting-Workflow:/opt/deepthunder -v $HOME/.Xauthority:/root/.Xauthority:rw -v /tmp/.X11-unix -t -i stevedore /bin/bash
