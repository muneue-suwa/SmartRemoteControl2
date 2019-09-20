#!/bin/bash

# Get path to this file
INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`

# gdrive
## Download gdrive
mkdir -p $INSTALL_SH_DIRNAME/tmp
GDRIVE_FILENAME=$INSTALL_SH_DIRNAME/tmp/gdrive-linux-rpi
if [ ! -f $GDRIVE_FILENAME ]; then
    wget "https://github.com/gdrive-org/gdrive/releases/download/2.1.0/gdrive-linux-rpi" -O $GDRIVE_FILENAME
fi
## Install gdrive
sudo cp $GDRIVE_FILENAME /usr/local/bin/
sudo chmod +x /usr/local/bin/gdrive-linux-rpi
echo -e '#!/bin/sh\n\ngdrive-linux-rpi $@' | sudo tee /usr/local/bin/gdrive
sudo chmod +x /usr/local/bin/gdrive
## gdrive setting
gdrive about && \
python3 $INSTALL_SH_DIRNAME/src/gdrive.py $INSTALL_SH_DIRNAME initialization
