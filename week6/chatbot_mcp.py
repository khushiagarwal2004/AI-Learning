from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_core.tools import tool
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()
llm=ChatGroq(model='llama-3.1-8b-instant')

# MCP Client
client=MultiServerMCPClient(
    {
        'arith':{
            'transport':'stdio',
            'command':'python',
            'args':[r'/Users/KhushiAgarwal/AI-Learning/week6/main.py']
        },
        'expense':{
            'transport':'streamable_http',
            'url':'https://weather-04edb44af709.fastmcp.app/mcp'
        }
    }
)

# state
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

async def build_graph():

    tools=await client.get_tools()
    print(tools)
    llm_with_tools=llm.bind_tools(tools)

    # graph nodes
    async def chat_node(state:ChatState):
        '''LLM node that may anser or request a tool call'''
        messages=state['messages']
        response=await llm_with_tools.ainvoke(messages)
        return {'messages':[response]}

    tool_node=ToolNode(tools)  # Execute tool calls

    # graph structure
    graph=StateGraph(ChatState)
    graph.add_node('chat_node',chat_node)
    graph.add_node('tools',tool_node)

    graph.add_edge(START,'chat_node')
    graph.add_conditional_edges('chat_node',tools_condition)
    graph.add_edge('tools','chat_node')

    chatbot=graph.compile()

    return chatbot

async def main():
    chatbot=await build_graph()

    result= await chatbot.ainvoke({'messages':[HumanMessage(content='Add an expense -Rs 500 on a udemy course on 10th NOv')]})
    print(result['messages'][-1].content)

if __name__=='__main__':
    asyncio.run(main())