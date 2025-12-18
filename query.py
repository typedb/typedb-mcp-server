import requests

TYPEDB_URL = "http://localhost:8000"
TYPEDB_USERNAME = "admin"
TYPEDB_PASSWORD = "password"


def get_auth_token() -> str:
    """Sign in to TypeDB and get an access token."""
    response = requests.post(
        f"{TYPEDB_URL}/v1/signin",
        json={"username": TYPEDB_USERNAME, "password": TYPEDB_PASSWORD}
    )
    response.raise_for_status()
    return response.json()["token"]


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
    token = get_auth_token()
    
    response = requests.post(
        f"{TYPEDB_URL}/v1/query",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "databaseName": database,
            "transactionType": transaction_type,
            "query": query,
            "commit": transaction_type in ("write", "schema")
        }
    )
    response.raise_for_status()
    return response.text
