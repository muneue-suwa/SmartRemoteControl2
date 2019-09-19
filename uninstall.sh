#!/bin/bash

# Get path to this file
INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`

# Remove setting/.smartrc.cfg
rm $INSTALL_SH_DIRNAME/setting/.smartrc.cfg

# Uninstall crontab
crontab -r
sudo crontab -r

# Uninstall smartrc
sudo rm /usr/local/bin/smartrc

# Uninstall pigpio
sudo systemctl disable pigpiod.service
sudo systemctl stop pigpiod.service

# Uninstall gdrive
bash $INSTALL_SH_DIRNAME/uninstall-gdrive.sh
