import requests
import config
from common import get_auth_token, handle_typedb_response


def list_users() -> str:
    """Get all users present on the server."""
    token = get_auth_token()
    response = requests.get(
        f"{config.TYPEDB_URL}/v1/users",
        headers={"Authorization": f"Bearer {token}"}
    )
    handle_typedb_response(response)
    return response.text


def create_user(username: str, password: str) -> str:
    """Create a new user on the server."""
    token = get_auth_token()
    response = requests.post(
        f"{config.TYPEDB_URL}/v1/users/{username}",
        headers={"Authorization": f"Bearer {token}"},
        json={"password": password}
    )
    handle_typedb_response(response)
    return f"User '{username}' created successfully"


def delete_user(username: str) -> str:
    """Delete a user from the server."""
    token = get_auth_token()
    response = requests.delete(
        f"{config.TYPEDB_URL}/v1/users/{username}",
        headers={"Authorization": f"Bearer {token}"}
    )
    handle_typedb_response(response)
    return f"User '{username}' deleted successfully"
