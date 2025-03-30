#!/bin/bash

# appディレクトリの作成
mkdir -p app/{domain,use_cases,interfaces/{api,persistence},infrastructure}

# __init__.py を各ディレクトリに配置
touch app/__init__.py

touch app/domain/__init__.py

touch app/use_cases/__init__.py

touch app/interfaces/__init__.py
touch app/interfaces/api/__init__.py
touch app/interfaces/persistence/__init__.py

touch app/infrastructure/__init__.py

# 各層の基本ファイルを作成
touch app/domain/account.py

touch app/use_cases/send_money.py

touch app/interfaces/api/account_controller.py
touch app/interfaces/persistence/account_repository.py

touch app/infrastructure/db.py

# アプリケーションのエントリポイント作成
touch app/main.py

# テスト用ディレクトリ・ファイル作成
mkdir -p tests

touch tests/__init__.py
touch tests/test_send_money.py
touch tests/test_account_repository.py

# requirements.txt 作成
touch requirements.txt

# README作成
touch README.md

# 完了メッセージ
echo "Project directories and files created successfully!"
