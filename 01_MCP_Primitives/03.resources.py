from mcp.server.fastmcp import FastMCP

mcp = FastMCP("resources")

@mcp.resource("config://appinfo.config")
def getconfig()->str:
    '''App configuration'''
    return "{'appname': 'resources'}"


@mcp.resource("users://{user_id}/profile")
def getprofile(user_id)->str:
    '''Get user profile by ID'''
    if user_id == "mahi":
        return "Mahi's profile"
    
    return "Invalid profile"


if __name__ == "__main__":
    mcp.run()