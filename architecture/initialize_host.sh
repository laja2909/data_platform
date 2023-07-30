#!/bin/bash

echo 'Shout: Initialize.sh script starts...'
echo 'Shout: Initializing host machine.'

echo 'Shout: install ansible and run playbook'
sudo apt-get update
sudo apt-get install -y python3-pip
sudo -H pip3 install ansible==5.9.0

echo 'Shout: ansible installed!'



