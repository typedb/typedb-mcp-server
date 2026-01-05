import requests
import config
from common import get_auth_token


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


def database_schema(name: str) -> str:
    """Get the complete database schema as TypeQL."""
    token = get_auth_token()
    response = requests.get(
        f"{config.TYPEDB_URL}/v1/databases/{name}/schema",
        headers={"Authorization": f"Bearer {token}"}
    )
    response.raise_for_status()
    return response.text
