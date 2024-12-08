#!/bin/bash

# Update package lists
sudo apt update

# Install required system packages
sudo apt install -y python3-pip python3-tk

# Install Python packages from requirements.txt
pip3 install -r requirements.txt
