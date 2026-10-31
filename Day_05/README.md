# Day 5 — First OpenAI API Call

## Objective

Connect Python to the OpenAI API and build a simple AI assistant using the OpenAI Python SDK.

## Topics Covered

- What an API is and how an LLM API works
- OpenAI API keys and secure environment variables
- Installing and using the OpenAI Python SDK
- Sending prompts to a language model
- Understanding `temperature` and `max_output_tokens`
- Building a basic AI text assistant

## Tools and Libraries

- Python
- Jupyter Notebook
- OpenAI Python SDK
- python-dotenv

## Project Structure

```text
Day_05/
├── 05_first_openai_api_call.ipynb
---05_AI_Text_Assistant
└── README.md
```

## Setup

Install the required packages:

```bash
pip install openai python-dotenv
```

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore`. Never commit your API key to GitHub.

## First API Request

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain artificial intelligence in simple words."
)

print(response.output_text)
```

## Key Concepts

| Parameter           | Purpose                          |
| ------------------- | -------------------------------- |
| `model`             | Selects the language model       |
| `input`             | Provides the prompt              |
| `temperature`       | Controls generation randomness   |
| `max_output_tokens` | Limits the maximum output length |

## Mini Project — AI Text Assistant

Built a Python function that:

- Accepts a user prompt
- Sends it to the OpenAI API
- Receives a model-generated response
- Prints the response in Jupyter Notebook

## Learning Outcome

Learned how to connect a Python application to a real language model through an API and build a basic AI-powered assistant.

**Important:** Keep API keys private and monitor API usage and costs.
