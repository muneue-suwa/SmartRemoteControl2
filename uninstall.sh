#!/bin/bash

# Uninstall crontab
crontab -r
sudo crontab -r

# Uninstall smartrc
sudo rm /usr/local/bin/smartrc
