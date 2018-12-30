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
    smartrc.py  # main，smartrc を RaspberryPI から直接コマンドで操作できるようにする．
    smartrc_slackbot/
      run.py  # main for slackbot
      slackbot_settings.py  
      # settig file of smartrc_slackbot
      # $ smartrc init で自動で作成
      plugins/
        __init__.py  # モジュールを示すためのファイル（要るのかな?）
        smartrc_bot.py  # mybot.plugins
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
```shell
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

## Slack など
`# smartrc` チャンネルを使う
