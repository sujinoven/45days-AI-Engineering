# Day 10 – Function Calling and Tools

## Objective

Learn how to connect an LLM with Python functions using OpenAI Function Calling, allowing an AI assistant to request external tools and use their results to answer user questions.

## Topics Covered

1. **Understanding Function Calling**
   - What function calling is.
   - Why AI applications need tools.
   - How an LLM requests a Python function.
   - Understanding the function-calling workflow.

2. **Creating Python Functions**
   - Defining reusable Python functions.
   - Passing arguments to functions.
   - Returning function results.
   - Testing functions independently.

3. **Defining Tools with JSON Schema**
   - Declaring function tools.
   - Defining function names and descriptions.
   - Specifying parameters and data types.
   - Using required fields and `additionalProperties`.
   - Understanding `strict=True`.

4. **Connecting Tools with the OpenAI API**
   - Using the Responses API.
   - Passing tools through the `tools` parameter.
   - Understanding `tool_choice`.
   - Inspecting function-call requests.
   - Extracting function arguments using `json.loads()`.

5. **Executing Functions and Returning Results**
   - Executing the requested Python function.
   - Understanding `call_id`.
   - Sending results using `function_call_output`.
   - Connecting requests using `previous_response_id`.
   - Receiving the final response from the model.

## Tools and Technologies

- Python
- Jupyter Notebook
- OpenAI Python SDK
- OpenAI Responses API
- JSON
- JSON Schema
- Python `json` library
- `python-dotenv`

## Project Structure

```text
Day_10/
├── 10_function_calling.ipynb
└── README.md
```

## Hands-on Project: AI Calculator Assistant

Build an AI-powered calculator that understands natural-language questions and requests Python functions to perform calculations.

### Example Input

```text
What is 125 multiplied by 8?
```

### Python Function

```python
def multiply(a, b):
    return a * b
```

### Expected Output

```text
125 multiplied by 8 is 1000.
```

### Features

- Define Python functions as AI tools.
- Describe tools using JSON Schema.
- Allow the model to request function calls.
- Extract function arguments from JSON.
- Execute functions in Python.
- Return tool results to the model.
- Generate a natural-language response.

## Additional Challenges

Extend the calculator by implementing:

- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)

Teach the AI assistant to select the appropriate function based on the user's question.

## Key Concepts Learned

| Concept | Description |
|---|---|
| Function Calling | Allows an LLM to request application functions |
| Tools | Functions made available to the model |
| JSON Schema | Defines function parameters and their types |
| `tool_choice` | Controls whether and how the model uses tools |
| `json.loads()` | Converts JSON arguments into Python objects |
| `call_id` | Identifies a particular function-call request |
| `function_call_output` | Sends the executed function result back to the model |
| `previous_response_id` | Connects the follow-up response to the previous response |

## Learning Outcome

By completing Day 10, I learned how to:

- Understand LLM function calling.
- Create and test Python functions.
- Define tools using JSON Schema.
- Connect Python functions with the OpenAI Responses API.
- Extract and process function arguments.
- Execute tool calls and return their results.
- Build a basic AI calculator assistant.

## Important Note

The model requests function calls, but the Python application executes the functions. Only explicitly permitted functions should be executed. Production applications should also handle multiple tool calls, invalid arguments, API errors, and incomplete responses.

## GitHub Commit

```bash
git add Day_10/
git commit -m "Complete Day 10 function calling and tools"
git push
```

**Day 10 Status:** Function Calling and AI Tools Practice