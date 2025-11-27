"""Schema resources for MCP server."""

from typing import Optional

from typedb.common.exception import TypeDBDriverException

from typedb_mcp.utils.connection import TypeDBConnection


class SchemaResource:
    """MCP resource for accessing TypeDB schema information."""

    def __init__(self, connection: TypeDBConnection):
        """Initialize schema resource.

        Args:
            connection: TypeDB connection manager
        """
        self.connection = connection

    def get_schema(self, database_name: Optional[str] = None) -> str:
        """Get the complete database schema as TypeQL.

        Args:
            database_name: Name of the database (if None, uses config default)

        Returns:
            Complete schema definition in TypeQL format

        Raises:
            ValueError: If database is not found or not specified
            Exception: If schema retrieval fails
        """
        # Use provided database name or fall back to config default
        db_name = database_name or self.connection.config.database

        if not db_name:
            raise ValueError("Database name must be provided either as parameter or in config")

        driver = self.connection.get_driver()
        database = driver.databases.get(db_name)

        if not database:
            raise ValueError(f"Database '{db_name}' not found")

        try:
            # Get schema from database
            schema = database.schema()
            return schema
        except TypeDBDriverException as e:
            raise Exception(f"Failed to retrieve schema from database '{db_name}': {e}") from e


