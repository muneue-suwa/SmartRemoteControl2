#!/bin/bash

# Uninstall crontab
crontab -r
sudo crontab -r

# Uninstall smartrc
sudo rm /usr/local/bin/smartrc

# Uninstall pigpio
sudo systemctl disable pigpiod.service
sudo systemctl stop pigpiod.service
