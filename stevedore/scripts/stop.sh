#!/bin/bash
#Stops all stevedore containers that are running
docker rm $(docker ps -a -q  --filter ancestor=stevedore)
