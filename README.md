# strands-test

AWSのエージェント開発フレームワークStrandsのハンズオンを実施します

## 概要

このリポジトリは、AWSのAIエージェント構築SDK「Strands Agents」を使用したハンズオン実装です。
Qiitaの記事「[AWSでAIエージェント構築に入門！StrandsをAgentCoreにデプロイしてみよう](https://qiita.com/minorun365/items/deb10c8e7a6b1219e595)」に基づいて実装しています。

## 前提条件

- Python 3.10以上
- AWSアカウント
- Amazon BedrockでClaudeモデルへのアクセスが有効化されていること

## セットアップ手順

### 1. リポジトリのクローン

```bash
git clone https://github.com/Skyryo/strands-test.git
cd strands-test
```

### 2. Python仮想環境の作成と有効化

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

### 3. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

### 4. AWS認証情報の設定

`.env.example`をコピーして`.env`ファイルを作成し、AWS認証情報を設定します。

```bash
cp .env.example .env
```

`.env`ファイルを編集して、以下の情報を設定してください：

```
AWS_ACCESS_KEY_ID=あなたのアクセスキーID
AWS_SECRET_ACCESS_KEY=あなたのシークレットアクセスキー
AWS_REGION=us-east-1
```

**⚠️ 注意**: `.env`ファイルは機密情報を含むため、Gitにコミットしないでください（`.gitignore`に含まれています）。

### 5. Amazon Bedrockでモデルを有効化

AWSコンソールでAmazon Bedrockにアクセスし、使用したいClaudeモデルへのアクセスをリクエストして有効化してください。

## 使用方法

### 基本的なエージェントの実行

```bash
python agent.py
```

このコマンドで、Strandsエージェントが起動し、サンプルクエリ「JAWS-UG主催のAI Builders Dayはどこで開催される？」に対する回答を生成します。

## ファイル構成

```
.
├── README.md           # このファイル
├── requirements.txt    # Pythonパッケージの依存関係
├── .env.example        # 環境変数の設定例
├── .gitignore         # Git除外設定
└── agent.py           # Strandsエージェントの実装
```

## 主な機能

- **Strands Agents SDK**: AWSが提供するオープンソースのAIエージェントSDK
- **Amazon Bedrock連携**: Claude等の大規模言語モデルを使用
- **シンプルな実装**: 最小限のコードでAIエージェントを構築

## 参考資料

- [Qiita記事: AWSでAIエージェント構築に入門！](https://qiita.com/minorun365/items/deb10c8e7a6b1219e595)
- [Strands Agents公式ドキュメント](https://strandsagents.com/latest/documentation/docs/)
- [AWS Bedrock公式ドキュメント](https://docs.aws.amazon.com/bedrock/)

## ライセンス

このプロジェクトはハンズオン学習用です。
