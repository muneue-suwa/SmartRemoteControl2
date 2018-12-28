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
Description:	Raspbian GNU/Linux 9.6 (stretch)
Release:	9.6
Codename:	stretch
```

#### Python
```
$ python3 --version
Python 3.5.3
```

#### venv について
`env` ディレクトリがあるとき
```shell-session:start_development
source env/bin/activate
```
`env` ディレクトリがないとき
```shell-session:start_development
python3 -m venv env && \
source env/bin/activate && \
pip install pip -U && \
pip install -r pypi_requirements
```

### 実装方法
- 赤外線送受信部：[pigpio library - Examples](http://abyz.me.uk/rpi/pigpio/examples.html) の `irrp.py` を改変する．
    - `irrp.py` は `Public Domain` であるため，改変，再配布が可能
- Google Homeとの連携：`IFTTT` と `slack` で行う．
- dataのバックアップとシェア
    - 親機（`parent`）：`slack` にファイルをアップロードする．
        - `crontab` で自動化，コマンドで制御
    - 子機（`child`）：親機がファイルをアップロードしたら，自動で更新する．
- コマンド名：`smartrc` (`smart remote control`)

## 参考文献
[格安スマートリモコンの作り方](https://qiita.com/takjg/items/e6b8af53421be54b62c9)
