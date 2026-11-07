# Day 25 – Agent Memory and State Management

## Objective

Understand how AI agents maintain context across interactions and build a basic memory-enabled assistant using Python and the OpenAI API.

The project demonstrates short-term conversation history, persistent long-term memory, and retrieving saved information when answering questions.

## Topics Covered

- State vs memory
- Short-term conversation memory
- Long-term memory
- Conversation history
- JSON-based persistent storage
- Saving and loading memory
- Memory retrieval
- Combining short-term and long-term memory
- Basic memory design and privacy considerations

## Tools and Libraries

- Python
- Jupyter Notebook
- OpenAI API
- `openai`
- `python-dotenv`
- `json`
- `pathlib`

## Project Structure

```text
Day_25/
├── 25_agent_memory.ipynb
├── agent_memory.json
└── README.md
```

## 1. Agent Without Memory

Created a basic assistant that sends independent requests to the OpenAI Responses API.

Observed that previous requests are not automatically included in a new API request.

## 2. Short-Term Memory

Created `conversation_history` to store user and assistant messages.

Built `chat_with_memory()` to send conversation history with each new request.

## 3. Long-Term Memory

Created a JSON-based memory system.

Implemented:

- `save_memory()` – saves information to a JSON file.
- `load_memory()` – loads previously saved information.

Tested persistent storage across notebook sessions.

## 4. Memory Retrieval

Created `ask_agent_with_long_term_memory()`.

The function loads saved information and includes it in the model's instructions so the assistant can use relevant facts when answering questions.

## 5. Combining Memory Systems

Created `memory_agent()` to combine:

- Short-term conversation history
- Long-term saved information

The assistant can use both sources of context when responding.

## Key Learning

State represents information needed during a workflow.

Short-term memory maintains conversation context, while long-term memory stores useful information for future sessions.

Memory must be designed carefully, with attention to privacy, accuracy, and storage limits.

## Next Step

**Day 26 – Agent Orchestration Frameworks**

Explore how orchestration frameworks help coordinate tools, workflows, state, and more complex agent systems.
