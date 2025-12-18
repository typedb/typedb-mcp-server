from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result.
    
    Args:
        a: The first number
        b: The second number
    
    Returns:
        The sum of a and b
    """
    return a + b * 2

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
