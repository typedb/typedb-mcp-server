# TypeDB MCP Server

An MCP (Model Context Protocol) server that enables AI assistants to interact with [TypeDB](https://typedb.com) databases. This allows LLMs to execute TypeQL queries, manage databases, and manage users through natural language.

## Features

- **Query Execution**: Run TypeQL read, write, and schema queries
- **Database Management**: List, create, and delete databases
- **User Management**: List, create, and delete users

## Running the Server

```bash
docker run -p 8001:8001 typedb/typedb-mcp-server:<version> \
  --typedb-address <address> \
  --typedb-username <username> \
  --typedb-password <password>
```

If you're running TypeDB server on `localhost`:
- replace `<address>` with `http://host.docker.internal:8000` instead of `http://localhost:8000`
- on Linux, add `--add-host=host.docker.internal:host-gateway`

## Using with Cursor IDE

1. Start the MCP server (see above)

2. Open Cursor Settings → MCP

3. Add the server configuration. Create or edit `.cursor/mcp.json` in your project:

```json
{
  "mcpServers": {
    "typedb": {
      "url": "http://localhost:8001/mcp"
    }
  }
}
```

4. Restart Cursor or refresh MCP connections

5. Start chatting! You can now ask Cursor to:
   - "List all databases"
   - "Create a database called 'mydb'"
   - "Define an entity 'person' with attribute 'name' in database 'mydb'"
   - "Insert a person with name 'Alice'"
   - "Query all persons in the database"

## Building from Source

Use `podman` or `Docker` to create a Docker image and push it to DockerHub:

```bash
podman login docker.io

VERSION=$(cat VERSION)
podman build -t typedb/typedb-mcp-server:$VERSION .
podman push typedb/typedb-mcp-server:$VERSION
```