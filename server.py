from fastmcp import FastMCP

mcp = FastMCP(
    "Math Tools",
    description="Provides mathematical operations like addition, subtraction, etc."
)

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result.
    
    Args:
        a: First number (e.g., 5.0, -3.14)
        b: Second number (e.g., 10, 2.5)
    
    Returns:
        The arithmetic sum of a and b
    
    Example:
        add(5, 3) returns 8
    """
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
