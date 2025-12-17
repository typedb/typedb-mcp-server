from fastmcp import FastMCP

mcp = FastMCP(
    name="TypeDB MCP Server",
    instructions="TODO",
    version="TODO",
    website_url="TODO",

    )

@mcp.tool
def add(num1: int, num2: int) -> int:
    return num1 + num2


@mcp.tool
def subtract(num1: int, num2: int) -> int:
    return num1 - num2


if __name__ == "__main__":
    mcp.run()
