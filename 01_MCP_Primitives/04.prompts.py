from mcp.server.fastmcp import FastMCP
from mcp.types import PromptMessage,TextContent
from mcp.server.fastmcp.prompts.base import UserMessage,AssistantMessage


mcp = FastMCP("prompts")



@mcp.prompt()
def getprompts(context:str)->str:
    '''Return prompt based on context'''
    return "Add 'Expand' to get more detail"

@mcp.prompt()
def getcustomprompt(context:str):
    return [
        UserMessage(f"Help me with {context}"),
        AssistantMessage(f"Sure here is the answer  --> 'cooking' for your question {context}")
    ]

# @mcp.prompt()
# def getprompts(context:str)->list[PromptMessage]:
#     '''Return prompt based on context'''
#     
#     message = PromptMessage(role="user",content=TextContent(type='text',text="Hello mr caller"))
#     return [message]



if __name__ == "__main__":
    mcp.run()