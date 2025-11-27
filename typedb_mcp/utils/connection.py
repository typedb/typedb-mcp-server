"""TypeDB connection management."""

from typing import Optional

import typedb.driver as typedb
from typedb.api.connection.driver import Driver
from typedb.api.connection.options import TypeDBOptions
from typedb.common.exception import TypeDBDriverException

from typedb_mcp.utils.config import TypeDBConfig


class TypeDBConnection:
    """Manages TypeDB driver connection."""

    def __init__(self, config: TypeDBConfig):
        """Initialize TypeDB connection manager.

        Args:
            config: TypeDB configuration
        """
        self.config = config
        self._driver: Optional[Driver] = None

    def connect(self) -> Driver:
        """Create and return a TypeDB driver connection.

        Returns:
            TypeDB Driver instance

        Raises:
            TypeDBDriverException: If connection fails
        """
        if self._driver is not None and self._driver.is_open():
            return self._driver

        try:
            # Create credentials if username/password are provided
            credentials = None
            if self.config.has_credentials():
                credentials = typedb.TypeDBCredential(
                    self.config.username,
                    self.config.password,
                    tls_enabled=False,  # Set to True for TypeDB Cloud
                )

            # Create driver options
            driver_options = TypeDBOptions()

            # Create driver
            self._driver = typedb.driver(
                self.config.address,
                credentials=credentials,
                driver_options=driver_options,
            )

            return self._driver
        except TypeDBDriverException as e:
            raise ConnectionError(f"Failed to connect to TypeDB at {self.config.address}: {e}") from e

    def close(self) -> None:
        """Close the TypeDB driver connection."""
        if self._driver is not None and self._driver.is_open():
            self._driver.close()
            self._driver = None

    def is_connected(self) -> bool:
        """Check if the driver is connected."""
        return self._driver is not None and self._driver.is_open()

    def get_driver(self) -> Driver:
        """Get the current driver, connecting if necessary."""
        if not self.is_connected():
            self.connect()
        return self._driver

