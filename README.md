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

#### venv について

`env` ディレクトリがあるとき

```shell
source env/bin/activate
```

`env` ディレクトリがないとき

```shell
python3 -m venv env && \
source env/bin/activate && \
pip install pip -U && \
pip install -r requirements.txt
```

## インストール

```shell
cd /to/the/application/path && \
sudo apt install -y python3-pip python3-requests pigpio git && \
pip3 install slackclient==1.3.0 --user && \
pip3 install pigpio==1.44 --user && \
git clone https://github.com/dongsiku/SmartRemoteControl2.git && \
bash SmartRemoteControl2/install.sh
```

### 実装方法

- 赤外線送受信部：[pigpio library - Examples](http://abyz.me.uk/rpi/pigpio/examples.html) の `irrp.py` を改変する．
  - `irrp.py` は `Public Domain` であるため，改変，再配布が可能
- Google Home との連携：`IFTTT` と `slack` で行う．
- data のバックアップとシェア
  - 受信機付き（`withRecord`）：`slack` にファイルをアップロードする．
    - `crontab` で自動化，コマンドで制御
  - 送信機のみ（`onlyPlayback`）：親機がファイルをアップロードしたら，自動で更新する．
- コマンド名：`smartrc` (`smart remote control`)

### 機能

- playback
- record
- share (upload_text, download_text)
- backup (upload_file)
- ~~log~~

## 参考文献

[格安スマートリモコンの作り方](https://qiita.com/takjg/items/e6b8af53421be54b62c9)
