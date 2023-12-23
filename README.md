# contract-ocr
契約書OCRによるOpenAI分析プロダクト

# サービス開発背景
OCRニーズは高く、項目チェックなどのオペレーション業務を自動化したいという企業が多い。
汎用的なOCRと項目抽出をプロダクト化することによって、同じようなケースに対して拡張性を持ったOCRプロダクトを開発する

# サービス概要
### サービス
契約書OCR

# 起動方法
```
// リポジトリのクローン
$ git clone git@github.com:quackshift-jp/contract-ocr.git

$ git switch main
$ git pull

// Python環境のアクティベート
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

// 環境変数のセット
$ cd path/to/contract-ocr
$ touch env

//以下を埋めて、envファイルを作成
OPENAI_API_KEY={APIキー}
DB_USER={ユーザー名}
DB_PASS={パスワード}
DB_HOST={ホスト}
DB_NAME={データベース名}
AWS_ACCESS_KEY_ID={AWSのアクセスきー}
AWS_SECRET_ACCESS_KEY={AWSのシークレットキー}


// FastAPIの起動
$ cd path/to/src && uvicorn backend.main:app --reload --port 8000

// Streamlitの起動
$ path/to/src && streamlit run frontend/app.py
```

### 主要機能
- 契約書アップロード
  - PDF or JPEGをアップする
  - OCRアルゴリズムによるテキスト検知を行う
  - OCRテキストから、対象項目のテキストを抽出する
  - 項目内容をチェックし、保存する
- ダッシュボード機能
  - 過去に保存された契約書内容とその更新時間を確認する
  - 


# 技術スタック
| 技術範囲 | 技術スタック |
| ---- | ---- |
| フロントエンド | Streamlit |
| バックエンド | FastAPI |
| データベース | PostgreSQL |
| ストレージ | Amazon S3 |
| デザイン | Figma |


# 今後の展望
1. EC2 or ECS + Fargateサーバーへのデプロイ
現状はローカルサーバーに置いており、ローカルコマンドからの起動が必要になっている。
AWSによる管理へと移行し、CI/CDパイプラインの開発も検討したい。

2. データベースの充実化
現状は、最低限のデータ保管しかしておらず、データ分析などができる状態にはなっていない。
そのため、データベースの設計からAPI開発に着手したい。

3. 項目チェック機能の拡張や、RAGを使った社内ドキュメントとの差分検知AIなど、新たな機能開発