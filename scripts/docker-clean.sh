#!/bin/sh

# Remove all images at once
docker rmi $(docker images -q)

# Stop all running containers: 
docker stop $(docker ps -a -q)
# Delete all stopped containers: 
docker rm $(docker ps -a -q)