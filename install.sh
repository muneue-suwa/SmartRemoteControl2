#!/bin/bash

# Get path to this file
INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`

installation()
{
  if [ ! -f $INSTALL_SH_DIRNAME/setting/smartrc.cfg ]; then
      echo "setting/smartrc.cfg was not found"
      echo "Please make the file referencing setting/smartrc.cfg.default"
      return 1
  fi

  # Make directories for log and data
  mkdir -p $INSTALL_SH_DIRNAME/log
  mkdir -p $INSTALL_SH_DIRNAME/data

  # Run smartrc.py init to make .smartrc.cfg
  python3 $INSTALL_SH_DIRNAME/src/smartrc.py init
  if [ ! -f $INSTALL_SH_DIRNAME/setting/.smartrc.cfg ]; then
      echo "Occured error when initializing smartrc"
      return 1
  fi

  # Install
  python3 $INSTALL_SH_DIRNAME/installation/make_installation_files.py $INSTALL_SH_DIRNAME
  ## pigpio
  sudo pigpiod
  sudo systemctl enable pigpiod.service
  sudo systemctl restart pigpiod.service
  ## crontab
  crontab $INSTALL_SH_DIRNAME/installation/smartrc_bot.crontab
  sudo crontab $INSTALL_SH_DIRNAME/installation/pigpiod.crontab
  ## smartrc
  sudo mv $INSTALL_SH_DIRNAME/installation/smartrc /usr/local/bin/
  sudo chmod +x /usr/local/bin/smartrc
}

installation
