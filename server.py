from fastmcp import FastMCP
from query import query as execute_query
from database import list_databases as db_list, create_database as db_create, delete_database as db_delete

mcp = FastMCP(
    "TypeDB MCP Server",
    # description="Provides query capability against a TypeDB server"
)

@mcp.tool
def query(query: str, database: str, transaction_type: str) -> str:
    """Executes given TypeQL query against the given database.
    
    Args:
        query: TypeQL query to be executed
        database: The name of the database against which the query will be executed
        transaction_type: Transaction type - "read" (for fetching data), "write" (for inserting data), or "schema" (for modifying the schema)
    
    Returns:
        Query results as JSON string
    
    Example:
        query("match $p isa person; fetch { $p.* };", "social_network")
    """
    return execute_query(query, database, transaction_type)


@mcp.tool
def database_list() -> str:
    """List all databases on the TypeDB server.
    
    Returns:
        JSON string containing list of databases
    """
    return db_list()


@mcp.tool
def database_create(name: str) -> str:
    """Create a new database on the TypeDB server.
    
    Args:
        name: Name of the database to create
    
    Returns:
        Success message
    """
    return db_create(name)


@mcp.tool
def database_delete(name: str) -> str:
    """Delete a database from the TypeDB server.
    
    Args:
        name: Name of the database to delete
    
    Returns:
        Success message
    """
    return db_delete(name)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8001)
