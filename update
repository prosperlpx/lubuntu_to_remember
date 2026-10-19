#!/bin/bash

#we are writing this for our universal update and install script for ubuntu and debian for now.
#other distros would be included later

dir=/usr/lib/os-release
ubuntu=ubuntu

if grep -q "$ubuntu" $dir || grep -q "$debian" $dir; then 
    sudo apt update && sudo apt upgrade -y && apt autoremove -y
fi
