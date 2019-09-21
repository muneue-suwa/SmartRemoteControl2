# Smart Remote Control with Google Home

## Hardware

詳細は [hardware.md](manuals/hardware.md) を参照すること．

## Software

### 環境

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

## インストール

1. ダウンロードと必要なアプリケーションのインストール

   ```shell
   cd /to/the/application/path && \
   sudo apt install -y python3-pip python3-requests pigpio git && \
   pip3 install slackclient==1.3.0 --user && \
   pip3 install pigpio==1.44 --user && \
   git clone https://github.com/dongsiku/SmartRemoteControl2.git
   ```

2. `SmartRemoteControl2/setting/smartrc.cfg`を作成する．（`SmartRemoteControl2/setting/smartrc.cfg.default`を参考にすること）
3. SmartRemoteControl2 のインストールを行う．

   ```shell
   bash SmartRemoteControl2/install.sh && \  # SmartRemoteControl2のインストール
   bash SmartRemoteControl2/install-gdrive.sh  # gdriveのインストール
   ```

### 実装方法

- 赤外線送受信部：[pigpio library - Examples](http://abyz.me.uk/rpi/pigpio/examples.html) の `irrp.py` を改変する．
  - `irrp.py` は `Public Domain` であるため，改変，再配布が可能
- Google Home との連携：`IFTTT` と `slack` で行う．
- data のバックアップとシェア：`Google drive` を利用する．
- コマンド名：`smartrc` (`SMART Remote Control`)

### 機能

- playback
- record
- share && backup: [gdrive_manual](manuals/gdrive_manual.md)
- ~~log~~

## 参考文献

[格安スマートリモコンの作り方](https://qiita.com/takjg/items/e6b8af53421be54b62c9)

```

```
