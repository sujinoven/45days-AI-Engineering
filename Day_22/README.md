# Day 22 – Introduction to AI Agents and Tool Use

## Objective

Understand the fundamentals of AI agents and build a simple tool-using AI agent with Python and the OpenAI API.

The project demonstrates how an LLM can request a tool, how the Python application executes it, and how the result is returned to the model to generate a final response.

## Topics Covered

- Introduction to AI agents
- Chatbots vs AI agents
- Agent workflow
- Tool calling and function execution
- Function schemas
- JSON arguments
- Executing tools with Python
- Returning tool results to the LLM
- Building a basic calculator agent

## Tools and Libraries

- Python
- Jupyter Notebook
- OpenAI API
- `openai`
- `python-dotenv`
- `json`

## Project Structure

```text
Day_22/
├── 22_introduction_to_ai_agents.ipynb
└── README.md
```

## 1. Introduction to AI Agents

Learned how an AI agent can understand a user's goal, decide which tool to use, request its execution, and use the result to respond.

Compared basic chatbots with tool-using AI agents.

## 2. Creating Python Tools

Created a Python multiplication function:

`multiply(a, b)`

The function accepts two numbers and returns their product.

## 3. Tool Schema

Defined a function tool schema for the OpenAI API.

The schema describes:

- Function name
- Function description
- Input parameters
- Required arguments
- Strict JSON schema validation

## 4. Tool Calling

Used the OpenAI Responses API to let the model request the multiplication tool.

Inspected the model response to identify:

- Function name
- JSON arguments
- Tool call ID

## 5. Tool Execution

Used Python to:

- Identify the requested function
- Parse the JSON arguments
- Execute the corresponding Python function
- Capture the result

## 6. Returning Tool Results

Sent the tool result back to the model using:

`function_call_output`

Used `previous_response_id` to continue the response workflow.

The model then generated a natural-language answer using the calculated result.

## 7. Calculator Agent

Created a reusable function:

`calculator_agent(question)`

The function connects the model's tool request, Python execution, and final answer generation.

Tested multiplication questions using different numbers.

## Agent Workflow

**User Request → LLM → Tool Selection → Python Execution → Tool Result → LLM → Final Answer**

## Key Learning

An AI agent can use tools to perform tasks beyond generating text.

The LLM decides which tool to request, but the application is responsible for executing the tool and returning its result.

The Day 22 calculator is a beginner-friendly example of a tool-using agent, not a fully autonomous production agent.

## Next Step

**Day 23 – Building More Capable AI Agents**

Continue exploring tool use, multiple tools, and agent workflows as part of Week 4: AI Agents and Orchestration.
