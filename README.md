# Smart Remote Control with Google Home

## Hardware

For details, see [hardware.md](manuals/hardware.md).

## Software

### Environment

#### Raspbian

```shell-session:rasbian_version
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Raspbian
Description:	Raspbian GNU/Linux 10 (buster)
Release:	10
Codename:	buster
```

#### Python

```shell
$ python3 --version
Python 3.7.3
```

## Preparation

### Slack

### IFTTT

### Google drive

## Installation

1. Install the additional packages for the application and download the application.

   ```shell
   cd /to/the/application/path && \
   sudo apt install -y python3-pip python3-requests pigpio git && \
   pip3 install slackclient==1.3.0 --user && \
   pip3 install pigpio==1.44 --user && \
   git clone https://github.com/dongsiku/SmartRemoteControl2.git
   ```

2. Create `setting/smartrc.cfg`. For example, see [setting/smartrc.cfg.default](setting/smartrc.cfg.default).

   ```ini
   [SLACK]
   SLACK_API_TOKEN = YOUR-SLACK-API-TOKEN

   [GDRIVE]
   ID = YOUR-GDRIVE-ID

   [BASIC]
   LOCATION = YOUR-SMARTRC-LOCATION-NAME
   is_WITH_RECODER = False

   [SLACKBOT]
   DEFAULT_REPLY = Sorry but I did not understand you

   [GPIO]
   RECORD = 18
   PLAYBACK = 17

   ```

3. Install this application.

   ```shell
   bash SmartRemoteControl2/install.sh && \  # Install SmartRemoteControl2
   bash SmartRemoteControl2/install-gdrive.sh  # Install gdrive
   ```

## Usage

This application is controled with `smartrc` (SMART Remote Control) command.

### Record and playback IR remote control codes

- To record IR remote control codes

  ```shell
  smartrc record IR_REMOTE_CONTROL_ID
  ```

  or

  ```shell
  smartrc learn IR_REMOTE_CONTROL_ID
  ```

- To playback IR remote control codes

  ```shell
  smartrc playback IR_REMOTE_CONTROL_ID
  ```

  or

  ```shell
  smartrc send IR_REMOTE_CONTROL_ID
  ```

### Backup, restore, and share the IR remote control codes data through gdrive (Google DRIVE)

**If you want to use these features, gdrive must be installed on the Raspberry Pi by [install-gdrive.sh](install-gdrive.sh).**

- To backup IR remote control codes

  ```shell
  smartrc backup
  ```

- To restore IR remote control codes

  ```shell
  smartrc recovery
  ```

- To share IR remote control codes

  This command makes Raspberry Pis having same slack channel and Google drive directory ID share their data. This command can be used on the Raspberry Pi set up as the Pi having recorder, because only this Pi can send the data.

  ```shell
  smartrc share
  ```

  or

  ```shell
  smartrc update
  ```

## Reference

[格安スマートリモコンの作り方](https://qiita.com/takjg/items/e6b8af53421be54b62c9)
