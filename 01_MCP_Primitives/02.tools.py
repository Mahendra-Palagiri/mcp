from mcp.server.fastmcp import FastMCP

mcp= FastMCP("tools-demo")


@mcp.tool()
def add(a:int, b:int)-> int:
    '''Add two numbers together'''
    return a+b

@mcp.tool()
def greet(name:str, formal:bool=False)->str:
    '''Greet someone. use Formal=True for a professional greeting.'''
    if formal:
        return f"Good day, {name}"
    return f"Hey, {name}"


if __name__ == "__main__":
    mcp.run()