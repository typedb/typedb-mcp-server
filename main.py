from fastmcp import FastMCP

@mcp.tool
def add(num1: int, num2: int) -> int:
    return num1 + num2


def main():
    print("Hello from typedb-mcp!")
    server = FastMCP[Any]("Demo")
    server.run()
    

if __name__ == "__main__":
    main()
