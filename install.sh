#!/bin/bash

INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`

mkdir -p $INSTALL_SH_DIRNAME/log
mkdir -p $INSTALL_SH_DIRNAME/data

python3 $INSTALL_SH_DIRNAME/crontab/make_crontab.py $INSTALL_SH_DIRNAME
crontab $INSTALL_SH_DIRNAME/crontab/smartrc_bot.crontab
