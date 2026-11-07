# Day 24 – Multi-Step Agent Workflows

## Objective

Build a multi-step AI workflow using Python and the OpenAI API.

The project demonstrates how multiple tools can work together, how intermediate results are stored, and how state is maintained throughout a workflow.

## Topics Covered

- Multi-step agent workflows
- Task decomposition
- Tool coordination
- Workflow orchestration
- State management
- Intermediate results
- Information retrieval
- Key-point extraction
- LLM-powered summarization
- Basic error handling

## Tools and Libraries

- Python
- Jupyter Notebook
- OpenAI API
- `openai`
- `python-dotenv`
- `json`

## Project Structure

```text
Day_24/
├── 24_multi_step_agent_workflows.ipynb
└── README.md
```

## 1. Creating Tools

Created three Python functions:

- `search_documents()` – searches a local knowledge base.
- `extract_key_points()` – extracts useful information from search results.
- `create_summary()` – generates a summary using the OpenAI API.

## 2. State Management

Created an `agent_state` dictionary to retain:

- Original goal
- Search results
- Extracted key points
- Final summary

## 3. Building the Workflow

Created `run_research_workflow()` to coordinate the steps.

The workflow:

1. Receives a user goal.
2. Searches the knowledge base.
3. Stores retrieved information.
4. Extracts key points.
5. Generates a summary.
6. Returns the final result and workflow state.

## 4. Error Handling

Added a check for empty search results.

When no documents match the query, the workflow returns a `no_results` status instead of generating a summary without supporting information.

## Workflow Architecture

**User Goal → Document Search → Key-Point Extraction → LLM Summary → Final Result**

## Key Learning

Multi-step workflows connect several operations to accomplish a larger task.

State management allows intermediate results to be preserved and reused.

This project uses a controlled Python workflow. It is not yet a fully autonomous agent.



## Next Step

**Day 25 – Agent Memory and State**

Learn how agents retain useful information and manage context across multiple steps and interactions.