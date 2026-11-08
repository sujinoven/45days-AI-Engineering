# Day 27 – Advanced Agent Workflows: Feedback Loops

## Objective

Build a cyclic AI workflow using LangGraph, Python, and the OpenAI API.

The project demonstrates how an agent workflow can generate an answer, review it, revise it when necessary, and stop when it meets basic quality requirements or reaches a revision limit.

## Topics Covered

- Linear and cyclic workflows
- Agent feedback loops
- Draft generation
- Review and refinement
- Conditional routing
- State management
- Revision counters
- Execution limits
- Workflow inspection
- Stopping conditions

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
Day_27/
├── 27_feedback_loop_agents.ipynb
└── README.md
```

## 1. Workflow State

Created an `AgentState` TypedDict to maintain:

- User question
- Retrieved documents
- Generated draft
- Review feedback
- Revision count
- Maximum revisions
- Approval status

## 2. Workflow Nodes

Created four nodes:

- `search_node()` – retrieves matching documents.
- `draft_node()` – generates an initial answer.
- `review_node()` – checks basic answer quality.
- `revision_node()` – improves the draft using review feedback.

## 3. Conditional Routing

Created `route_after_review()` to decide whether the workflow should:

- Finish when the answer is approved.
- Finish when the revision limit is reached.
- Revise the answer when improvement is needed.

## 4. Feedback Loop

Connected the revision node back to the review node.

This allows the workflow to repeat the review and revision process until it passes the check or reaches its maximum number of revisions.

## 5. Workflow Architecture

**START → Search → Draft → Review**

If approved:

**Review → END**

If improvement is needed:

**Review → Revise → Review**

The workflow uses a revision limit to prevent endless execution.

## Key Learning

Cyclic workflows allow agents to review and improve intermediate results.

State preserves the draft, feedback, and revision count across workflow steps.

Stopping conditions are essential for controlling execution and API costs.

The quality check in this project is a simple deterministic demonstration, not a comprehensive evaluation system.

## Next Step

**Day 28 – Knowing When Not to Use an Agent**

Learn how to choose between simple Python workflows, LLM-powered workflows, and autonomous agents based on task complexity, cost, reliability, and control.
