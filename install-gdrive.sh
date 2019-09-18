#!/bin/bash

# gdrive
## Download gdrive
if [ ! -f $INSTALL_SH_DIRNAME/tmp/gdrive-linux-rpi ]; then
    curl -JLO --create-dirs -o $INSTALL_SH_DIRNAME/tmp \
    "https://docs.google.com/uc?id=0B3X9GlR6EmbnVXNLanp4ZFRRbzg&export=download"
fi
## Install gdrive
sudo cp $INSTALL_SH_DIRNAME/tmp/gdrive-linux-rpi /usr/local/bin/
sudo chmod +x /usr/local/bin/gdrive-linux-rpi
echo -e '#!/bin/sh\n\ngdrive-linux-rpi $@' | sudo tee /usr/local/bin/gdrive
sudo chmod +x /usr/local/bin/gdrive
## gdrive setting
gdrive about
gdrive sync download [ID] $INSTALL_SH_DIRNAME/setting
