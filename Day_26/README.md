# Day 26 – Agent Orchestration with LangGraph

## Objective

Understand agent orchestration frameworks and build a graph-based research workflow using LangGraph, Python, and the OpenAI API.

The project demonstrates how nodes, edges, conditional routing, and shared state can coordinate a multi-step AI workflow.

## Topics Covered

- Introduction to agent orchestration
- LangGraph fundamentals
- Graph-based workflows
- State management
- Nodes and edges
- Conditional routing
- Graph compilation
- Workflow execution
- Comparing LangGraph, smolagents, and LlamaIndex

## Tools and Libraries

- Python
- Jupyter Notebook
- LangGraph
- OpenAI API
- `langgraph`
- `openai`
- `python-dotenv`

## Project Structure

```text
Day_26/
├── 26_langgraph_orchestration.ipynb
└── README.md
```

## 1. Defining Workflow State

Created a `ResearchState` TypedDict to define the information shared across the graph:

- Research goal
- Search results
- Extracted key points
- Final summary

## 2. Creating Graph Nodes

Created four nodes:

- `search_node()` – searches the local knowledge base.
- `extract_node()` – extracts key points from retrieved documents.
- `summary_node()` – generates a summary using the OpenAI API.
- `no_results_node()` – handles queries without matching documents.

## 3. Conditional Routing

Created `route_after_search()` to decide which node should execute next.

If search results exist, the graph continues to extraction.

If no results exist, the graph returns a no-results message.

## 4. Building the Graph

Used `StateGraph` to:

- Register nodes.
- Define the starting point.
- Connect workflow steps.
- Add conditional edges.
- Define ending points.
- Compile the graph.

## 5. Running the Workflow

Executed the compiled graph using `app.invoke()`.

Inspected the resulting state, retrieved documents, extracted key points, and generated summary.

## Workflow Architecture

**START → Search → Conditional Routing → Extract → Summarize → END**

If no documents match:

**START → Search → No Results → END**

## Framework Comparison

- LangGraph: stateful graph-based agent orchestration.
- smolagents: lightweight framework for building tool-using agents.
- LlamaIndex: framework focused on LLM applications and data workflows.

## Key Learning

Orchestration frameworks organize how an AI workflow executes.

LangGraph uses nodes, edges, and shared state to coordinate tasks and conditional execution.

This project is a controlled graph workflow, not yet an autonomous planning agent.

## Next Step

**Day 27 – Agent Workflows and Orchestration Patterns**

Continue exploring more complex workflows and how agents coordinate multiple tools and tasks.
