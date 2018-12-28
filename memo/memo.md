# Memo

## Python のバージョン
```
$ python3 --version
Python 3.5.3
```

## 機能
- init (update)
  - `smartrc.cfg` の内容を確認し，`.smartfc.cfg` を作成する．
  - `slack` の `token` 等を確認する．
- send (playback)
  - 赤外線を送信する
  - `playback.py`
- learn (record)
  - 赤外線を学習する
  - `send.py`
- backup
  - Slack に `data/` のファイルをアップロードし，バックアップする．
  - `backup.py`
- recovery
  - Slack にアップロードファイルをダウンロード，リカバリーする．
  - `download.py`
- share
  - 受信機能のついたものからついていないものに学習したデータを送信する
  - `download.py` && `upload.py`

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
  src/
    smartrc.py  # main
    record.py  # gpio 関連
    playback.py  # gpio 関連
    download.py  # file 関連
    upload.py  # file 関連
    irrp_2.py
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
```
export PATH=${PATH}:/to/the/smartrc.sh/path
```

## Slack など
`# smartrc` チャンネルを使う
