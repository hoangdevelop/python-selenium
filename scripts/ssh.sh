#!/bin/sh

chmod 400 ec2.pem
ssh -i "ec2.pem" ec2-user@ec2-34-214-157-16.us-west-2.compute.amazonaws.com
