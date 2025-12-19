import asyncio
from fastmcp import Client
from server import mcp


async def main():
    async with Client(mcp) as client:
        result = await client.call_tool("database_schema", {
            "name": "test2"
        })
        print("Result:", result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
