# TODO
- get the outer layer working:
    - start/stop mcp server
    - make llm able to use add/subtract appropriately

# API
info:
    inform the user that this is for executing a single query into typedb
configs:
    - typedb server
tools:
    query
        database: ...
        type: write/read/schema
        impl:
          transform human language into query?
          execute typedb http endpoint

    user: create, update, delete (later)
    database: create, delete (later)
resources:
    user: list & detail
    database: list & schema