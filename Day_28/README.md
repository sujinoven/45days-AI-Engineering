# Day 28 – Knowing When Not to Use an AI Agent

## Objective

Understand when to use a traditional Python workflow, an LLM-powered workflow, or an AI agent.

The project demonstrates how to choose an appropriate architecture based on task requirements, complexity, flexibility, cost, and predictability.

## Topics Covered

- Traditional Python workflows
- LLM-powered workflows
- AI agents
- Deterministic vs dynamic execution
- Agent complexity
- Model calls and cost considerations
- Reliability and predictability
- Choosing the simplest effective architecture
- Human oversight and risk management

## Tools and Libraries

- Python
- Jupyter Notebook

## Project Structure

```text
Day_28/
├── 28_when_not_to_use_agents.ipynb
└── README.md
```

## 1. Comparing Three Approaches

Studied three application architectures:

- Python Workflow – predefined logic and deterministic execution.
- LLM Workflow – uses an LLM for a specific language-related task.
- AI Agent – can select tools and adapt its next actions based on observations.

## 2. Building a Decision System

Created `choose_approach()` to recommend an architecture based on task requirements.

The function considers:

- Language understanding
- Multiple dynamic steps
- External tool requirements

## 3. Testing Example Tasks

Tested the decision system with examples involving:

- Monthly expense calculations
- Customer review summarization
- Company research and competitor comparison

## 4. Cost and Complexity Comparison

Compared the approaches using illustrative model-call counts, complexity, and predictability.

Learned that more autonomous systems can introduce additional API costs, latency, and operational complexity.

## Key Learning

The most sophisticated architecture is not always the best architecture.

Use Python for clear, rule-based tasks, LLM workflows for focused language tasks, and agents when tasks require adaptive, multi-step decisions.

Start with the simplest reliable solution and introduce agent capabilities only when they provide meaningful value.

## Week 4 Complete

Explored AI agents, multiple tools, multi-step workflows, memory, LangGraph orchestration, feedback loops, and the decision of when not to use agents.

## Next Step

**Week 5 – Evaluation, Observability, and LLMOps**

Learn how to measure AI application quality, detect failures, monitor behavior, and improve reliability.
