#!/bin/bash

#we are writing this for our universal update and install script

ubuntu_dir=/etc/apt;

if [ -d $ubuntu_dir ]; then 
   #the host is based on debain or ubuntu,
   #run the apt version of the command

  sudo apt update && sudo apt dist-upgrade -y
fi 
