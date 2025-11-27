"""Main MCP server for TypeDB."""

import asyncio
import sys
from urllib.parse import parse_qs, urlparse

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Resource, Uri

from typedb_mcp.resources.schema import SchemaResource
from typedb_mcp.utils.config import TypeDBConfig
from typedb_mcp.utils.connection import TypeDBConnection


class TypeDBMCPServer:
    """MCP server for TypeDB."""

    def __init__(self, config: TypeDBConfig | None = None):
        """Initialize the TypeDB MCP server.

        Args:
            config: TypeDB configuration (if None, loads from environment)
        """
        if config is None:
            config = TypeDBConfig()

        self.config = config
        self.connection = TypeDBConnection(config)
        self.schema_resource = SchemaResource(self.connection)
        self.server = Server("typedb-mcp")

        # Register resources
        self._register_resources()

    def _register_resources(self) -> None:
        """Register MCP resources."""
        # Register schema resource
        @self.server.list_resources()
        async def list_resources() -> list[Resource]:
            """List available resources."""
            return [
                Resource(
                    uri=Uri("typedb://schema"),
                    name="Schema",
                    description="Complete database schema in TypeQL format. Use query parameter 'database' to specify database name (e.g., typedb://schema?database=my_db)",
                    mimeType="text/plain",
                ),
            ]

        @self.server.read_resource()
        async def read_resource(uri: Uri) -> str:
            """Read a resource by URI.

            Args:
                uri: Resource URI (may include query parameter 'database')

            Returns:
                Resource content as string

            Raises:
                ValueError: If URI is not recognized
            """
            uri_str = str(uri)
            parsed = urlparse(uri_str)

            # Extract database name from query parameters
            database_name = None
            if parsed.query:
                query_params = parse_qs(parsed.query)
                if "database" in query_params:
                    database_name = query_params["database"][0]

            try:
                if parsed.scheme == "typedb" and parsed.netloc == "schema":
                    return self.schema_resource.get_schema(database_name=database_name)
                else:
                    raise ValueError(f"Unknown resource URI: {uri_str}")
            except Exception as e:
                raise ValueError(f"Failed to read resource {uri_str}: {e}") from e

    async def run(self) -> None:
        """Run the MCP server."""
        # Connect to TypeDB
        try:
            self.connection.connect()
            print(f"Connected to TypeDB at {self.config.address}", file=sys.stderr)
        except Exception as e:
            print(f"Failed to connect to TypeDB: {e}", file=sys.stderr)
            sys.exit(1)

        # Run the server
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options(),
            )

    def cleanup(self) -> None:
        """Clean up resources."""
        self.connection.close()


async def main() -> None:
    """Main entry point for the MCP server."""
    server = TypeDBMCPServer()
    try:
        await server.run()
    except KeyboardInterrupt:
        pass
    finally:
        server.cleanup()


if __name__ == "__main__":
    asyncio.run(main())

