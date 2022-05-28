FROM python:3.8
# 基本的には標準のpythonから作成する

ENV APP_PATH=/code \
    PYTHONPATH=.
#　開発物のソースコードはcodeデイレクトリ下に配置する

WORKDIR $APP_PATH

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y libgl1-mesa-dev poppler-utils poppler-data && \
    pip install poetry
# コンテナのセットアップ

COPY . .

RUN poetry install
#　必要なパッケージ等をインストールする

EXPOSE 8000