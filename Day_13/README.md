# Day 13 – AI-Powered Contact Extractor CLI

## Objective

Build a command-line AI application that extracts contact information from unstructured text and returns clean, structured JSON using the OpenAI API.

## Topics Covered

- OpenAI Responses API
- Structured Outputs
- JSON schema
- Extracting information from unstructured text
- Converting JSON into Python dictionaries
- Function calling and tools
- Executing model-requested Python functions
- Building command-line applications (CLI)
- Basic error handling

## Tools and Technologies

- Python
- Jupyter Notebook
- OpenAI Python SDK
- OpenAI Responses API
- JSON
- python-dotenv

## Project Structure

```text
Day_13/
├── 13_contact_extractor.ipynb
├── contact_extractor.py
└── README.md
```

## Practical Exercises

### 1. Contact Extraction

Created a function called `extract_contact()` that extracts:

- Name
- Email
- Company

The function uses the OpenAI API and a JSON schema to ensure structured output.

### 2. JSON Schema

Defined a schema with:

- Required fields
- String and null data types
- Strict structured output
- No additional properties

Missing information is represented as `null` rather than invented.

### 3. Function Calling

Created a Python tool called `count_words()`.

The model can request this function, while the Python application executes it and handles the result.

### 4. Command-Line Interface

Built `contact_extractor.py`, which:

- Accepts text from the terminal.
- Sends the text to the OpenAI API.
- Extracts contact information.
- Displays the result as formatted JSON.
- Handles errors gracefully.

## Example Input

```text
Hello!

My name is David Miller.
I work at Microsoft.
My email is david@microsoft.com.
```

## Expected Output

```json
{
    "name": "David Miller",
    "email": "david@microsoft.com",
    "company": "Microsoft"
}
```

## Key Concepts Learned

| Concept | Description |
|---|---|
| Structured Outputs | Producing output that follows a defined structure |
| JSON Schema | Defining the expected output fields and types |
| `json.loads()` | Converting JSON text into Python objects |
| Function Calling | Allowing a model to request application tools |
| CLI | Interacting with an application through a terminal |
| Error Handling | Managing failures without unexpected crashes |

## Learning Outcomes

By completing Day 13, I learned how to:

- Extract structured information from messy text.
- Use JSON schemas with the OpenAI API.
- Build reusable Python functions.
- Implement function calling.
- Execute model-requested tools.
- Build a basic AI-powered command-line application.

## How to Run

From the repository root:

```bash
python Day_13/contact_extractor.py
```

Make sure your `.env` file contains your OpenAI API key and that the required Python packages are installed.

## GitHub Commit

```bash
git add Day_13/
git commit -m "Complete Day 13 AI contact extractor CLI"
git push
```

## Resources

- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [OpenAI API Documentation](https://platform.openai.com/docs/overview)

---

**Day 13 Status:** Complete after finishing the notebook, CLI project, quiz, and GitHub commit.