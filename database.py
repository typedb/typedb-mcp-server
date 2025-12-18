import requests
import config


def get_auth_token() -> str:
    """Sign in to TypeDB and get an access token."""
    response = requests.post(
        f"{config.TYPEDB_URL}/v1/signin",
        json={"username": config.TYPEDB_USERNAME, "password": config.TYPEDB_PASSWORD}
    )
    response.raise_for_status()
    return response.json()["token"]


def list_databases() -> str:
    """Get all databases present on the server."""
    token = get_auth_token()
    response = requests.get(
        f"{config.TYPEDB_URL}/v1/databases",
        headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
    return response.text


def create_database(name: str) -> str:
    """Create a database on the server."""
    token = get_auth_token()
    response = requests.post(
        f"{config.TYPEDB_URL}/v1/databases/{name}",
        headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
    return f"Database '{name}' created successfully"


def delete_database(name: str) -> str:
    """Delete a database from the server."""
    token = get_auth_token()
    response = requests.delete(
        f"{config.TYPEDB_URL}/v1/databases/{name}",
        headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
    return f"Database '{name}' deleted successfully"
