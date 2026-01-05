import requests
import config
import json


def get_auth_token() -> str:
    """Sign in to TypeDB and get an access token."""
    response = requests.post(
        f"{config.TYPEDB_URL}/v1/signin",
        json={"username": config.TYPEDB_USERNAME, "password": config.TYPEDB_PASSWORD}
    )
    handle_typedb_response(response)
    return response.json()["token"]


def handle_typedb_response(response: requests.Response) -> None:
    """Check response status and raise an error with TypeDB error details if needed.
    
    This ensures that TypeDB error messages are properly extracted from the response
    and propagated to the MCP client.
    
    Args:
        response: The requests.Response object to check
        
    Raises:
        requests.HTTPError: If the response status indicates an error, with TypeDB error details included
    """
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        # Try to extract error details from TypeDB response
        error_data = response.json()
        http_error = requests.HTTPError(error_data, response=response)
        raise http_error from e
