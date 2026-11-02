# Day 08 — Prompt Engineering Fundamentals

## Objective

Learn how to write effective prompts and guide Large Language Models (LLMs) to generate useful, relevant, and structured responses.

## Topics Covered

- Introduction to prompt engineering
- System/developer instructions vs user messages
- Role prompting
- Context prompting
- Few-shot prompting
- Reasoning instructions
- Comparing weak and improved prompts
- Calling the OpenAI API with different prompts

## Tools and Technologies

- Python
- Jupyter Notebook
- OpenAI Python SDK
- python-dotenv
- OpenAI Responses API

## Project Structure

```text
Day_08/
├── 08_prompt_engineering.ipynb
└── README.md
```

## Hands-on Project — Prompt Engineering Lab

Built a Python-based prompt-testing lab using the OpenAI API.

The project includes:

1. Connecting to the OpenAI API.
2. Creating a reusable `ask_ai()` function.
3. Testing a simple prompt.
4. Improving the prompt with role instructions and context.
5. Experimenting with few-shot prompting for sentiment classification.
6. Comparing the outputs produced by different prompts.

## Prompting Techniques Learned

| Technique | Explanation |
|---|---|
| Role prompting | Assigning a specific role to the model |
| Context prompting | Providing relevant background information |
| Few-shot prompting | Providing examples of desired input and output |
| Reasoning instructions | Asking the model to solve a task carefully and explain key steps |

## System/Developer Instructions vs User Messages

- **System/developer instructions:** Define the assistant's behavior, role, and constraints.
- **User message:** Contains the actual task or question.

Both help guide the model's response.

## Example — Reusable API Function

```python
def ask_ai(instructions, user_prompt):

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=instructions,
        input=user_prompt
    )

    return response.output_text
```

This function accepts instructions and a user prompt, sends them to the OpenAI API, and returns the generated response.

## Learning Outcome

Learned how to design effective prompts, provide relevant context, use examples to guide model responses, and compare different prompting approaches through practical API experiments.

## Key Takeaway

Good prompt engineering is about providing clear instructions, useful context, and a well-defined task so that an LLM produces the desired output.

