from fastmcp import FastMCP

mcp = FastMCP(
    name="TypeDB MCP Server",
    instructions="A Model Context Protocol server for interacting with TypeDB databases. Provides tools for executing queries and managing TypeDB resources.",
    version="0.1.0",
    website_url="https://github.com/typedb/typedb-mcp-server",
)

@mcp.tool
def add(num1: int, num2: int) -> int:
    """Add two numbers together.
    
    Args:
        num1: The first number to add
        num2: The second number to add
    
    Returns:
        The sum of num1 and num2
    """
    return num1 + num2


@mcp.tool
def subtract(num1: int, num2: int) -> int:
    """Subtract the second number from the first number.
    
    Args:
        num1: The number to subtract from
        num2: The number to subtract
    
    Returns:
        The difference of num1 and num2
    """
    return num1 - num2


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
