from fastmcp import FastMCP

mcp = FastMCP(
    "TypeDB MCP Server",
    description="Provides query capability against a TypeDB server"
)

@mcp.tool
def query(query: str, database: str) -> str:
    f"""Executes given query against the given database.
    
    Args:
        query: TypeQL query to be executed
        database: The name of the database against which the query will be executed
    
    Returns:
        query answers
    
    Example:
        query("match $p isa user; get;", "users")"
    """
    return "henlo" # TODO: query typedb database

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
