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


def list_databases() -> str:
    """Get all databases present on the server."""
    token = get_auth_token()
    response = requests.get(
        f"{TYPEDB_URL}/v1/databases",
        headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
    return response.text


def create_database(name: str) -> str:
    """Create a database on the server."""
    token = get_auth_token()
    response = requests.post(
        f"{TYPEDB_URL}/v1/databases/{name}",
        headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
    return f"Database '{name}' created successfully"


def delete_database(name: str) -> str:
    """Delete a database from the server."""
    token = get_auth_token()
    response = requests.delete(
        f"{TYPEDB_URL}/v1/databases/{name}",
        headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
    return f"Database '{name}' deleted successfully"
