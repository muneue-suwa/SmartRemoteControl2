# Memo

## Python のバージョン
```
$ python3 --version
Python 3.5.3
```

## 機能
- init (update)
  - `setting/smartrc.cfg` の内容を確認し，設定ファイルを作成する．
    - `setting/.smartfc.cfg`
    - `src/smartrc_slackbot/slackbot_settings.py`
  - `slack` の `token` 等を確認する．
- send (playback)
  - 赤外線を送信する
  - `playback.py`
- learn (record)
  - 赤外線を学習する
  - `send.py`
- backup
  - Slack に `data/` のファイルをアップロードし，バックアップする．
  - `backup_irrp_2_json.py`
- recovery
  - Slack にアップロードファイルをダウンロード，リカバリーする．
  - `download.py`
- share
  - 受信機能のついたものからついていないものに学習したデータを送信する
  - `download.py` && `upload.py`
- list
  - `irrp_2.json` を読み込み，`rcd_ply_id` のリストを表示する
  - `read_rcd_ply_idlist.py`

### Raspberry PI から
`init (update)`, `send (playback)`, `learn (record)`, `backup`, `recovery`, `share`, `list`

### Google Home（slack） から
`send (playback)`, `list`

### コマンド
- backup: `smartrc backup`
- share: `smartrc share`
- send (playback): `smartrc send *`, `smartrc playback *`
- learn (record): `smartrc learn *`, `smartrc record *`
- recovery: `smartrc recovery`
- init: `smartrc init`

## tree
```
SmartRemoteControl2/
  data/
    smartrc_yyyymmdd_hhmmss.irrp
  src/
    smartrc.py  # main，smartrc を RaspberryPI から直接コマンドで操作できるようにする．
    run.py  # main for slackbot
    record.py  # gpio 関連
    playback.py  # gpio 関連
    download.py  # file 関連
    upload.py  # file 関連
    irrp_with_class.py
    config.py
    backup_irrp_file.py
  log/
  setting/
    smartrc.cfg.default  # defaultのもの
    smartrc.cfg
    .smartrc.cfg  # 確認されたもの
  smartrc.sh
  install.sh
  uninstall.sh
```

## smartrc.cfg
- mode: 受信機能付きか，送信機能のみか
- slackのtoken
- その他設定が必要なもの

## install.sh
```bash
export PATH=${PATH}:/to/the/smartrc.sh/path
```

## listen_to() in slackbot/slackbot/bot.py
```python
def listen_to(matchstr, flags=0):
    def wrapper(func):
        PluginsManager.commands['listen_to'][
            re.compile(matchstr, flags)] = func
        logger.info('registered listen_to plugin "%s" to "%s"', func.__name__,
                    matchstr)
        return func

    return wrapper
```

## share() について
`irrp_2_*.json` の中身を文字列に変えて，slackにメッセージとしてアップする．
1. `from_smartrc_bot [filename] START_IRRP_FILE [data_1]`
1. `from_smartrc_bot [filename] CONTINUE_IRRP_FILE [data_2]`
1. `from_smartrc_bot [filename] CONTINUE_IRRP_FILE [data_3]`
1. `from_smartrc_bot [filename] CONTINUE_IRRP_FILE [data_n]`
1. `from_smartrc_bot [filename] END_IRRP_FILE`

```python
import json
from pprint import pprint


f = open("temp.json", "r")  # upload
json_file = json.load(f)
string = str(json_file).replace("'", '"').replace(" ", "")
print("len:", len(string))
print("string:", string)
f.close()

f2 = open("temp.temp", "w")  # download
f2.write(string+"\n")
f2.close()

f3 = open("temp.temp", "r")  # checking
json_file_3 = json.load(f3)
pprint(json_file_3)
f3.close()
```

## Slack など
`# smartrc` チャンネルを使う
