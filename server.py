from fastmcp import FastMCP
from query import query as execute_query

mcp = FastMCP(
    "TypeDB MCP Server",
    # description="Provides query capability against a TypeDB server"
)

@mcp.tool
def query(query: str, database: str, transaction_type: str = "read") -> str:
    """Executes given TypeQL query against the given database.
    
    Args:
        query: TypeQL query to be executed
        database: The name of the database against which the query will be executed
        transaction_type: Transaction type - "read", "write", or "schema" (default: "read")
    
    Returns:
        Query results as JSON string
    
    Example:
        query("match $p isa person; fetch { $p.* };", "social_network")
    """
    return execute_query(query, database, transaction_type)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8001)
