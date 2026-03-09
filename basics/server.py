from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Hello-World")


# Type hints --> MCP auto-generates the JSON Schema from the tool (i.e. "name: str" tells the client that the tool expects a string argument called 'name')
@mcp.tool() #Registers the function as a callable tool
def greet(name: str) -> str:
    '''Say hello to someone by name.''' #Docstring becomes the Tool description 
    return f"Hello, {name}!"


if __name__ =="__main__":
    mcp.run()
