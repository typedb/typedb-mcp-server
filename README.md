# TypeDB MCP Server

A Model Context Protocol (MCP) server for TypeDB, enabling AI assistants and other MCP clients to interact with TypeDB databases through a standardized interface.

## Overview

This MCP server provides tools and resources for:
- Executing TypeQL queries and analyzing query plans
- Managing database transactions
- Exploring graph structures and concepts
- Accessing schema information

## Features

### MCP Resources
- **Schema Access**: Retrieve complete database schemas as TypeQL (supports multi-tenancy via database parameter)

### MCP Tools
- **Query Execution**: Run and analyze TypeQL queries
- **Transaction Management**: Open, commit, and close transactions
- **Graph Exploration**: Navigate concepts, attributes, and relations

## Installation

### Prerequisites
- Python 3.9+
- TypeDB Server (running locally or remotely)
- TypeDB database

### Setup

1. Clone the repository:
```bash
git clone https://github.com/vaticle/typedb-mcp.git
cd typedb-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables (see Configuration section)

## Configuration

### Environment Variables

Set the following environment variables. You can either:
- Create a `.env` file from `.env.example` and fill in your values
- Export them in your shell
- Pass them when running the server

Required variables:
- `TYPEDB_HOST`: TypeDB server host (default: `localhost`)
- `TYPEDB_PORT`: TypeDB server port (default: `1729`)

Optional variables:
- `TYPEDB_DATABASE`: Default database name (can also be specified per resource request)

Optional variables (only if TypeDB server has authentication enabled):
- `TYPEDB_USERNAME`: Username for authentication
- `TYPEDB_PASSWORD`: Password for authentication

### Quick Setup

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` with your TypeDB connection details:
```bash
# Edit .env file
TYPEDB_HOST=localhost
TYPEDB_PORT=1729
TYPEDB_DATABASE=my_database
# Add credentials if needed:
# TYPEDB_USERNAME=admin
# TYPEDB_PASSWORD=password
```

## Usage

### Running the MCP Server

```bash
python -m typedb_mcp.server
```

### Docker (Coming Soon)

```bash
docker run \
  -e TYPEDB_HOST=localhost \
  -e TYPEDB_PORT=1729 \
  -e TYPEDB_DATABASE=my_database \
  -e TYPEDB_USERNAME=admin \
  -e TYPEDB_PASSWORD=password \
  typedb-mcp
```

## Development

### Project Structure

```
typedb-mcp/
├── typedb_mcp/          # Main package
│   ├── server.py        # MCP server implementation
│   ├── tools/           # MCP tools
│   ├── resources/       # MCP resources
│   └── utils/           # Utility functions
├── tests/               # Test suite
├── PLAN.md              # Implementation plan
└── README.md            # This file
```

### Running Tests

```bash
pytest tests/
```

## MCP Tools Reference

### Core Tools
- `run_query`: Execute a TypeQL query
- `analyze_query`: Analyze a query without executing
- `open_transaction`: Open a new transaction
- `commit_transaction`: Commit a write transaction
- `close_transaction`: Close a transaction
- `transaction_run_query`: Execute query in transaction context
- `transaction_run_analyze`: Analyze query in transaction context

### Exploration Tools
- `get_concept_with_attribute`: Find concepts by attribute value
- `get_attributes_by_concept`: Get all attributes of a concept
- `get_relations_of_concept`: Find relations where a concept participates
- `get_players_of_relation`: Get all players in a relation

## MCP Resources Reference

- `schema`: Complete database schema in TypeQL format
  - URI: `typedb://schema`
  - Query parameter: `database` (optional) - database name to query
  - Example: `typedb://schema?database=my_database`
  - If database parameter is not provided, uses the default from `TYPEDB_DATABASE` environment variable

## Contributing

Contributions are welcome! Please see our contributing guidelines (coming soon).

## License

[License TBD]

## Related Projects

- [TypeDB](https://github.com/vaticle/typedb)
- [TypeDB Python Driver](https://github.com/vaticle/typedb-python)
- [Model Context Protocol](https://modelcontextprotocol.io/)

