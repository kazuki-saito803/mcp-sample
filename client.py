import asyncio
from fastmcp import Client

async def test_calls():
    async with Client("http://localhost:8000/mcp") as client:
        # ツール一覧を確認
        tools = await client.list_tools()
        print("Available tools:", [t for t in tools])

        # リソース一覧もしくは取得
        config = await client.read_resource("app://config")
        print("Config resource:", config)

        profile = await client.read_resource("user://Alice")
        print("User profile for Alice:", profile)

        # プロンプトを取得して使う例
        prompt_text = await client.get_prompt("ask_for_sum", {"nums": [1, 2, 3, 4]})
        print("Prompt for sum:", prompt_text)

        # ツール呼び出し
        greeting = await client.call_tool("greet", {"name": "Bob"})
        print("Greet tool:", greeting)

        total = await client.call_tool("sum_numbers", {"nums": [10, 20, 30]})
        print("Sum tool:", total)

        data = await client.call_tool("fetch_data", {"key": "alpha"})
        print("Fetched data:", data)

if __name__ == "__main__":
    asyncio.run(test_calls())