#!/bin/bash

# Get path to this file
INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`

# Make directories for log and data
mkdir -p $INSTALL_SH_DIRNAME/log
mkdir -p $INSTALL_SH_DIRNAME/data

# Install crontab
python3 $INSTALL_SH_DIRNAME/installation/make_crontab.py $INSTALL_SH_DIRNAME
crontab $INSTALL_SH_DIRNAME/installation/smartrc_bot.crontab

# Install smartrc
