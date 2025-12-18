import asyncio
from fastmcp import Client
from server import mcp


async def main():
    async with Client(mcp) as client:
        result = await client.call_tool("query", {
            "query": "match $p isa user; get;",
            "database": "users"
        })
        assert result.content[0].text == "henlo"

if __name__ == "__main__":
    asyncio.run(main())
