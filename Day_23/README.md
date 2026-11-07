# Day 23 – Building Multi-Tool AI Agents

## Objective

Build a multi-tool AI agent using Python and the OpenAI Responses API.

The project demonstrates how an LLM can select from multiple tools, request their execution, observe the results, and continue working through a multi-step workflow.

## Topics Covered

- The think, act, observe loop
- Multi-tool AI agents
- Function calling
- Tool schemas
- Python tool registry
- Tool dispatch and execution
- Argument validation
- Multiple function calls
- Multi-step workflows
- Returning tool results to the model
- Basic agent execution limits

## Tools and Libraries

- Python
- Jupyter Notebook
- OpenAI API
- `openai`
- `python-dotenv`
- `json`

## Project Structure

```text
Day_23/
├── 23_multi_tool_agents.ipynb
└── README.md
```

## 1. Creating Python Tools

Created four calculator functions:

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`

Added division-by-zero handling.

## 2. Registering Tools

Created function schemas to describe the available tools to the OpenAI model.

Each schema defines:

- Function name
- Description
- Input parameters
- Required arguments
- Strict JSON schema validation

## 3. Tool Registry

Created a Python dictionary named `tool_registry`.

It maps function names to approved Python functions, allowing the application to select and execute the requested tool.

## 4. Tool Execution and Validation

Created `execute_tool()` to:

- Check whether a requested tool exists.
- Validate the supplied arguments.
- Reject invalid argument types.
- Execute the registered Python function.
- Return the result.

## 5. Multi-Tool Agent

Created `run_agent()` to manage the agent workflow.

The function:

1. Sends the user question to the model.
2. Inspects the model response for function calls.
3. Executes requested tools.
4. Collects tool results.
5. Sends results back to the model.
6. Repeats until the model returns a final response.

## Agent Architecture

**User Goal → Model → Tool Selection → Python Execution → Tool Results → Model → Final Answer**

The agent follows the think, act, observe pattern.

## Key Learning

A multi-tool agent can select from several approved functions and use their results in a multi-step workflow.

The Python application remains responsible for validating and executing tool requests.

This project is a foundation for more capable agents that use web search, RAG retrieval, APIs, and orchestration frameworks.

## Next Step

**Day 24 – Multi-Step Agent Workflows**

Continue building agents that can plan and execute more complex tasks using multiple tools and intermediate results.
