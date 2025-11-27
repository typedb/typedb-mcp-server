# TypeDB MCP Server - Implementation Plan

## Overview

This document outlines the plan for building a Model Context Protocol (MCP) server for TypeDB, enabling AI assistants and other MCP clients to interact with TypeDB databases through a standardized interface.

## Architecture

### Dependencies
- **TypeDB Python Driver**: Official TypeDB Python SDK for database connectivity
- **MCP Python SDK**: The `mcp` Python package for MCP server implementation
- **Deployment**: Docker container (implementation details TBD - see Future Considerations)

## MCP Resources

Resources provide read-only access to schema information:

1. **get schema**
   - Returns the complete database schema
   - Format: TypeQL schema definition
   - Supports multi-tenancy: database name can be passed as a query parameter in the URI
   - URI format: `typedb://schema?database=<database_name>`
   - If database parameter is omitted, uses default from configuration

## MCP Tools

### Core Tools

These tools provide direct query execution and transaction management:

1. **run_query**
   - **Args**: `query` (string) - TypeQL query to execute
   - **Returns**: Query response/result
   - **Description**: Execute a TypeQL query in a read transaction

2. **analyze_query**
   - **Args**: `query` (string) - TypeQL query to analyze
   - **Returns**: Analysis response (query plan, optimization info, etc.)
   - **Description**: Analyze a query without executing it

3. **open_transaction**
   - **Args**: `type` (string) - Transaction type ("read" or "write")
   - **Returns**: Transaction ID (string)
   - **Description**: Open a new transaction and return its identifier

4. **commit_transaction**
   - **Args**: `transaction_id` (string) - Transaction ID to commit
   - **Returns**: Commit result (success/failure)
   - **Description**: Commit a write transaction

5. **close_transaction**
   - **Args**: `transaction_id` (string) - Transaction ID to close
   - **Returns**: Success confirmation
   - **Description**: Close a transaction (read or write)

6. **transaction_run_query**
   - **Args**: `transaction_id` (string), `query` (string) - Transaction ID and TypeQL query
   - **Returns**: Query response/result
   - **Description**: Execute a query within a specific transaction context

7. **transaction_run_analyze**
   - **Args**: `transaction_id` (string), `query` (string) - Transaction ID and TypeQL query
   - **Returns**: Analysis response
   - **Description**: Analyze a query within a specific transaction context

### Exploration Tools

These tools provide convenient ways to explore the graph structure:

1. **get_concept_with_attribute**
   - **Args**: 
     - `attribute_type` (string) - Type of the attribute
     - `attribute_value` (string) - Value of the attribute
   - **Returns**: List of IIDs (Instance IDs) matching the criteria
   - **Description**: Find concepts (entities/relations) that have a specific attribute value

2. **get_attributes_by_concept**
   - **Args**: `iid` (string) - Instance ID of the concept
   - **Returns**: JSON object with all attributes of the concept
   - **Description**: Retrieve all attributes owned by a specific concept

3. **get_relations_of_concept**
   - **Args**: `iid` (string) - Instance ID of the concept
   - **Returns**: List of relation IIDs along with the role played by the concept
   - **Description**: Find all relations where a concept participates and the role it plays

4. **get_players_of_relation**
   - **Args**: `iid` (string) - Instance ID of the relation
   - **Returns**: List of role+player pairs
   - **Description**: Get all players (concepts) in a relation and their respective roles

## Implementation Phases

### Phase 1: Core Infrastructure
- [ ] Set up project structure
- [ ] Initialize MCP server with Python SDK
- [ ] Configure TypeDB connection
- [ ] Basic error handling and logging

### Phase 2: MCP Resources
- [ ] Implement `get_schema` resource
- [ ] Implement `get_schema_functions` resource
- [ ] Implement `get_schema_types` resource
- [ ] Test resource endpoints

### Phase 3: Core Tools
- [ ] Implement `run_query` tool
- [ ] Implement `analyze_query` tool
- [ ] Implement transaction management tools:
  - [ ] `open_transaction`
  - [ ] `commit_transaction`
  - [ ] `close_transaction`
- [ ] Implement transaction-scoped query tools:
  - [ ] `transaction_run_query`
  - [ ] `transaction_run_analyze`
- [ ] Add transaction state management

### Phase 4: Exploration Tools
- [ ] Implement `get_concept_with_attribute`
- [ ] Implement `get_attributes_by_concept`
- [ ] Implement `get_relations_of_concept`
- [ ] Implement `get_players_of_relation`

### Phase 5: Testing & Documentation
- [ ] Unit tests for all tools and resources
- [ ] Integration tests with TypeDB
- [ ] API documentation
- [ ] Usage examples

### Phase 6: Docker Deployment
- [ ] Create Dockerfile
- [ ] Configure container orchestration (TBD - discuss with team)
- [ ] Environment variable configuration
- [ ] Health checks
- [ ] Documentation for deployment

## Future Considerations

### Docker Deployment
- **Status**: Pending discussion
- **Questions to resolve**:
  - Container orchestration approach (Docker Compose, Kubernetes, etc.)
  - Configuration management (environment variables, config files)
  - Connection pooling and resource management
  - Scaling strategy
  - Health check endpoints

### Additional Features (Potential)
- Query result caching
- Batch query execution
- Schema validation tools
- Query optimization suggestions
- Performance monitoring/metrics

## Notes

- The exploration tools provide a GraphQL-like interface for traversing the TypeDB graph, which may be useful for AI assistants that need to explore the database structure.
- Transaction management allows for multi-step operations and write transactions.
- All tools should include proper error handling and validation of inputs.

