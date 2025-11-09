from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
import os
from dotenv import load_dotenv
from typing import Annotated
from langgraph.graph.message import AnyMessage, add_messages, BaseMessage
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import ArxivQueryRun, TavilySearchResults
from langchain_community.utilities import ArxivAPIWrapper
from langchain_core.tools import tool

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['TAVILY_API_KEY'] = os.getenv('TAVILY_API_KEY')


llm = init_chat_model("openai:gpt-4o")

class State(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]

def make_default_graph():
    graph_workflow = StateGraph(State)
    
    @tool
    def add(a:int, b:int):
        """Add two numbers"""
        return a+b
    
    arxiv_api_wrapper = ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=1000)
    arxiv = ArxivQueryRun(api_wrapper=arxiv_api_wrapper)

    tavily = TavilySearchResults()

    tools = [add, arxiv, tavily]
    llm_with_tools = llm.bind_tools(tools)

    def call_llm(state):
        return {'messages':[llm_with_tools.invoke(state['messages'])]}

    graph_workflow.add_node('call_llm', call_llm)
    graph_workflow.add_node('tools', ToolNode(tools))

    graph_workflow.add_edge(START, 'call_llm')
    graph_workflow.add_conditional_edges(
        "call_llm",
        tools_condition
    )
    graph_workflow.add_edge('tools', 'call_llm')

    agent = graph_workflow.compile()
    return agent

agent = make_default_graph()