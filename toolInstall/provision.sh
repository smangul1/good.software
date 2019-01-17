#!/bin/bash

# this script run when spinning up a Vagrant machine
yum install epel-release -y
yum update -q -y
yum install java-1.8.0-devel -y
yum install wget -y
yum install vim -y 
yum install unzip -y
yum install gcc gcc-devel -y
yum install python -y
yum install R -y
