"""Configuration management for TypeDB MCP server."""

import os
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class TypeDBConfig:
    """Configuration for TypeDB connection."""

    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        database: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ):
        """Initialize TypeDB configuration from parameters or environment variables.

        Args:
            host: TypeDB server host (defaults to TYPEDB_HOST env var or 'localhost')
            port: TypeDB server port (defaults to TYPEDB_PORT env var or 1729)
            database: Database name (defaults to TYPEDB_DATABASE env var)
            username: Username for authentication (defaults to TYPEDB_USERNAME env var)
            password: Password for authentication (defaults to TYPEDB_PASSWORD env var)
        """
        self.host = host or os.getenv("TYPEDB_HOST", "localhost")
        self.port = port or int(os.getenv("TYPEDB_PORT", "1729"))
        self.database = database or os.getenv("TYPEDB_DATABASE")
        self.username = username or os.getenv("TYPEDB_USERNAME")
        self.password = password or os.getenv("TYPEDB_PASSWORD")

        # Database is optional since it can be passed per request

    @property
    def address(self) -> str:
        """Get the TypeDB server address."""
        return f"{self.host}:{self.port}"

    def has_credentials(self) -> bool:
        """Check if credentials are provided."""
        return bool(self.username and self.password)

