# Dockerfile

FROM python:3.11-slim

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係をコピー
COPY ./requirements.txt /app/requirements.txt

# 依存ライブラリのインストール
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# ソースコードをコピー
COPY ./app /app/app

# FastAPIを8000ポートで起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
