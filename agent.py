from dotenv import load_dotenv
from strands import Agent

# .envファイルから環境変数を読み込む
# Load environment variables from .env file
load_dotenv()

# Strandsエージェントを作成
# Create Strands Agent
# デフォルトでBedrockのClaude Sonnet 4を使用
# Uses Bedrock's Claude Sonnet 4 by default
agent = Agent()

# エージェントに質問を投げる
# Ask a question to the agent
agent("JAWS-UG主催のAI Builders Dayはどこで開催される？")
