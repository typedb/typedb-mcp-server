import pytest
from fastmcp import Client
from server import mcp


@pytest.mark.anyio
async def test_query_tool():
    async with Client(mcp) as client:
        result = await client.call_tool("query", {
            "query": "match $p isa user; get;",
            "database": "users"
        })
        assert result[0].text == "henlo"
