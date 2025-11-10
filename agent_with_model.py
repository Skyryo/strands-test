from dotenv import load_dotenv
from strands import Agent

# .envファイルから環境変数を読み込む
# Load environment variables from .env file
load_dotenv()

# 特定のモデルを指定してStrandsエージェントを作成
# Create Strands Agent with a specific model
# Claude Haiku 4.5モデルを使用する例
# Example using Claude Haiku 4.5 model
agent = Agent("jp.anthropic.claude-haiku-4-5-20251001-v1:0")

# エージェントに質問を投げる
# Ask a question to the agent
agent("JAWS-UG主催のAI Builders Dayはどこで開催される？")
