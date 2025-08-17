from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage, SystemMessage
from typing import List


class OverallState(TypedDict):
    messages: List
class InputState(TypedDict):
    question: str
class OutputState(TypedDict):
    answer: str

# Tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

# LLM with bound tool
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools([multiply])

# Node
def tool_calling_llm(state):
    # If messages don't exist, create them from the question
    if "messages" not in state or not state["messages"]:
        messages = [
            SystemMessage(content="You are a helpful assistant. Only use the multiply tool when the user specifically asks for multiplication. For greetings and general questions, respond normally without using any tools."),
            HumanMessage(content=state.get("question", ""))
        ]
    else:
        messages = state["messages"]
    
    # Get LLM response
    response = llm_with_tools.invoke(messages)
    return {"messages": messages + [response]}

def generate_final_answer(state):
    last_message = state["messages"][-1]
    return {"answer": last_message.content}

# Build graph
builder = StateGraph(OverallState, input=InputState, output=OutputState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode([multiply]))
builder.add_node("generate_answer", generate_final_answer)

builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    tools_condition,
    {
        "tools": "tools",
        "__end__": "generate_answer"  # Go to answer generation instead of END
    }
)
builder.add_edge("tools", "tool_calling_llm")  # After tools, go back to LLM for final response
builder.add_edge("generate_answer", END)

# Compile graph
graph = builder.compile()