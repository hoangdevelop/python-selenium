#!/bin/sh
chmod 400 ec2.pem
ssh -i "ec2.pem" ec2-user@ec2-34-214-157-16.us-west-2.compute.amazonaws.com

# sudo amazon-linux-extras install docker
# sudo service docker start
# sudo systemctl enable docker

# sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# sudo chmod +x /usr/local/bin/docker-compose

# docker-compose version
