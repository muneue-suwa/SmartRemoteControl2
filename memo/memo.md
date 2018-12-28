# Memo

## 機能
- backup: `backup.py`
- share: `download.py` && `upload.py`
- send (playback): `playback.py`
- learn (record): `send.py`
- recovery: `download.py`
- init (update): `slack` の `token` 等を確認する．

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
  smartrc.sh  # ~/bin に link する
  install.sh
  uninstall.sh
```

## smartrc.cfg
- mode: 受信機能付きか，送信機能のみか
- slackのtoken
- その他設定が必要なもの

## Slack など
`# smartrc` チャンネルを使う
