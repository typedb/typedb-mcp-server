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
        error_message = f"TypeDB error (HTTP {response.status_code})"
        
        try:
            # TypeDB typically returns JSON error responses
            error_data = response.json()
            if isinstance(error_data, dict):
                # Extract common error fields
                if "message" in error_data:
                    error_message = f"TypeDB error: {error_data['message']}"
                elif "error" in error_data:
                    error_message = f"TypeDB error: {error_data['error']}"
                else:
                    # Include the full error data if available
                    error_message = f"TypeDB error: {json.dumps(error_data)}"
            elif isinstance(error_data, str):
                error_message = f"TypeDB error: {error_data}"
        except (ValueError, json.JSONDecodeError):
            # If response is not JSON, try to get text
            try:
                error_text = response.text
                if error_text:
                    error_message = f"TypeDB error: {error_text}"
            except Exception:
                pass  # Fall back to default error message
        
        # Create a new HTTPError with the enhanced error message
        # Preserve the original response object
        http_error = requests.HTTPError(error_message, response=response)
        raise http_error from e
