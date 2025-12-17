from fastmcp import FastMCP

mcp = FastMCP("TypeDB MCP Server")

@mcp.tool
def add(num1: int, num2: int) -> int:
    return num1 + num2


if __name__ == "__main__":
    mcp.run()
