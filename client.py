import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print("Available tools:", [t.name for t in tools.tools])
            
            # Call the add tool
            # result = await session.call_tool("add", {"a": 5, "b": 3})
            # print("add(5, 3) =", result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
