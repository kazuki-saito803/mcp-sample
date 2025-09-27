from fastmcp import FastMCP, Context
from typing import List, Dict

mcp = FastMCP("MyExpandedMCP")

# — Tool を追加 —  
@mcp.tool()
def greet(name: str) -> str:
    """指定された名前への挨拶を返す"""
    return f"Hello, {name}!"

@mcp.tool()
def sum_numbers(nums: List[int]) -> int:
    """整数リストの合計を返す"""
    return sum(nums)

@mcp.tool()
async def fetch_data(ctx: Context, key: str) -> Dict[str, str]:
    """
    仮の外部データ取得をシミュレートするツール。
    Context を使ってログを出したり進捗報告も可能。
    """
    await ctx.info(f"Fetching data for key = {key}")
    # ここでは擬似的にデータを返す
    return {"key": key, "value": f"value_for_{key}"}

# — Resource を追加 —  
# 静的リソース例
@mcp.resource("app://config")
def get_config() -> Dict[str, str]:
    """アプリケーションの設定情報を返すリソース"""
    return {
        "version": "1.0.0",
        "maintainer": "YourName",
        "features": "greet, sum, fetch"
    }

# 動的テンプレート URI リソース（URI の中にパラメータ {name} を含む例）
@mcp.resource("user://{name}")
def get_user_profile(name: str) -> Dict[str, str]:
    """ユーザープロファイル情報を返すリソース"""
    # 実際には DB などから取る想定
    return {
        "name": name,
        "role": "user",
        "welcome_msg": f"Welcome, {name}!"
    }

# — Prompt を追加 —  
@mcp.prompt()
def ask_for_sum(nums: list[int]) -> str:
    """合計を求めるプロンプトテンプレート"""
    return "次の数字の合計を求めてください：" + ", ".join(str(n) for n in nums)

@mcp.prompt()
def greet_user(name: str) -> str:
    """挨拶を促すプロンプトテンプレート"""
    return f"Hi, my name is {name}. Nice to meet you!"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)