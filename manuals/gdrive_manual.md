# インストール

gdrive のダウンロード先である Google Drive のリンクの詳細は [gdrive_GitHub](https://github.com/prasmussen/gdrive) を参照すること.

## 本番環境

ダウンロード，インストールを行う．

```shell-session:install_gdrive-linux-rpi
cd ~ && \
curl -JLO "https://github.com/gdrive-org/gdrive/releases/download/2.1.0/gdrive-linux-rpi" && \
sudo mv gdrive-linux-rpi /usr/local/bin/ && \
sudo chmod +x /usr/local/bin/gdrive-linux-rpi && \
echo -e '#!/bin/sh\n\ngdrive-linux-rpi $@' | sudo tee /usr/local/bin/gdrive && \
sudo chmod +x /usr/local/bin/gdrive && \
gdrive about && \
mkdir -p data/ && \
gdrive sync download [ID] data/
```

## 使用方法

`[ID]` は Google Drive の `AudioFiles` のディレクトリの ID を参照すること

### アップロード

```shell-session:gdrive_upload
gdrive sync upload data/ [ID]
```

### ダウンロード

```shell-session:gdrive_download
gdrive sync download [ID] data/
```
