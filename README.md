# LangGraph Template Repository

A starter template for building AI applications with LangGraph, featuring multiple examples and patterns to help you get started quickly.

## 🚀 What is LangGraph?

LangGraph is a library for building stateful, multi-actor applications with LLMs. It extends the LangChain expression language with the ability to coordinate multiple chains (or actors) across multiple steps of computation in a cyclic manner.

## 📁 Repository Structure

```
langgraph-temp/
├── README.md                 # This file
├── requirements.txt          # Main project dependencies
└── studio/                   # LangGraph Studio examples
    ├── agent.py             # Agent with tool calling example
    ├── simple.py            # Basic conditional routing example
    ├── router.py            # Tool routing example
    ├── langgraph.json       # Studio configuration
    └── requirements.txt     # Studio-specific dependencies
```

## 🛠️ Examples Included

### 1. **Simple Conditional Routing** (`studio/simple.py`)
A basic example demonstrating conditional edges and state management:
- Shows how to create nodes that modify state
- Demonstrates conditional routing based on state
- Uses a simple string-based state to track mood

### 2. **Agent with Tool Calling** (`studio/agent.py`)
A more advanced example with LLM agent and tools:
- Integrates OpenAI's GPT-4 with custom tools
- Demonstrates arithmetic operations (add, multiply, divide)
- Shows how to bind tools to an LLM and handle tool calls

### 3. **Tool Router** (`studio/router.py`)
A streamlined tool calling example:
- Focuses on the core tool calling pattern
- Shows how to route between LLM and tool execution
- Demonstrates the `tools_condition` pattern

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (for examples using GPT models)
- LangSmith API key (optional, for tracing and debugging)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd langgraph-temp
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment:**
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   export LANGCHAIN_API_KEY="your-langsmith-api-key-here"  # Optional
   export LANGCHAIN_TRACING_V2="true"  # Optional: Enable tracing
   export LANGCHAIN_PROJECT="langgraph-template"  # Optional: Set project name
   ```

### Running Examples

#### Basic Example
```bash
cd studio
python simple.py
```

#### Agent Example
```bash
cd studio
python agent.py
```

#### Router Example
```bash
cd studio
python router.py
```

## 🎯 Using LangGraph Studio

This repository includes LangGraph Studio configuration for interactive development:

## 🔍 Using LangSmith for Tracing

LangSmith provides powerful debugging and monitoring capabilities for your LangGraph applications:

### Setting Up LangSmith

1. **Get your API key:**
   - Sign up at [LangSmith](https://smith.langchain.com/)
   - Navigate to your API keys section
   - Copy your API key

2. **Configure environment variables:**
   ```bash
   export LANGCHAIN_API_KEY="your-langsmith-api-key-here"
   export LANGCHAIN_TRACING_V2="true"
   export LANGCHAIN_PROJECT="your-project-name"
   ```

3. **View traces in LangSmith:**
   - Run your LangGraph applications
   - Visit [LangSmith](https://smith.langchain.com/) to see detailed traces
   - Monitor execution flow, token usage, and performance

### What LangSmith Shows You

- **Execution Flow**: Visual representation of your graph execution
- **Node Performance**: Timing and token usage for each node
- **State Changes**: How state evolves through your graph
- **Tool Calls**: Detailed information about tool execution
- **Error Tracking**: Debug issues with detailed error information

1. **Install LangGraph CLI:**
   ```bash
   pip install langgraph-cli[inmem]
   ```

2. **Start Studio:**
   ```bash
   cd studio
   langgraph studio
   ```

3. **Open your browser** to the provided URL (usually `http://localhost:8123`)

## 🔧 Key Concepts Demonstrated

### State Management
- **MessagesState**: For conversational applications
- **Custom State**: For application-specific state tracking

### Graph Building
- **Nodes**: Individual processing units
- **Edges**: Connections between nodes
- **Conditional Edges**: Dynamic routing based on state

### Tool Integration
- **Tool Definition**: Creating custom functions
- **Tool Binding**: Attaching tools to LLMs
- **Tool Routing**: Handling tool calls and responses

## 📚 Learning Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph Tutorials](https://langchain-ai.github.io/langgraph/tutorials/)
- [LangGraph Studio Guide](https://langchain-ai.github.io/langgraph/tutorials/studio/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [LangSmith Tracing Guide](https://docs.smith.langchain.com/tracing/)

## 🤝 Contributing

Feel free to:
- Add new examples
- Improve existing examples
- Update documentation
- Report issues

## 📄 License

This template is provided as-is for educational and development purposes.

---

**Happy building with LangGraph! 🎉**
