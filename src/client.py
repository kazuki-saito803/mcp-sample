import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

async def setup():
    # MCP サーバーに接続してツール一覧・説明を取得
    async with client:
        tools = await client.list_tools()
        # tools はメタ情報（名前、説明、引数仕様など）を含む
        return tools

# asyncio.run(call_tool("Ford"))
result = asyncio.run(setup())
print(result)