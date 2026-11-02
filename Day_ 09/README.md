# Day 09 – Structured Outputs and JSON

## Objective

Learn how to make an LLM return structured JSON data that Python applications can easily read, validate, and process.

## Topics Covered

1. **JSON Fundamentals**
   - What JSON is and why it is used.
   - JSON data types: strings, numbers, booleans, arrays, objects, and null.
   - Understanding JSON structure.

2. **Working with JSON in Python**
   - Using Python's built-in `json` library.
   - `json.loads()` – converting JSON text into a Python dictionary.
   - `json.dumps()` – converting Python data into JSON text.
   - Accessing individual values from dictionaries.

3. **LLM JSON Responses**
   - Asking an LLM to return JSON.
   - Parsing the model's response using `json.loads()`.
   - Handling invalid or empty responses.

4. **OpenAI Structured Outputs**
   - Understanding JSON Schema.
   - Defining required fields and data types.
   - Using `strict=True`.
   - Preventing additional properties.
   - Handling missing information using `null`.

## Tools and Technologies

- Python
- Jupyter Notebook
- OpenAI Python SDK
- OpenAI Responses API
- Python `json` library
- JSON Schema
- `python-dotenv`

## Project Structure

```text
Day_09/
├── 09_structured_outputs_json.ipynb
└── README.md
```

## Hands-on Project: Contact Information Extractor

Build a small AI-powered application that extracts contact information from unstructured text.

### Input Example

```text
Hello,

My name is Sarah Johnson.
You can reach me at sarah@example.com.
I work at Google.
```

### Expected JSON Output

```json
{
    "name": "Sarah Johnson",
    "email": "sarah@example.com",
    "company": "Google"
}
```

### Features

- Extract names, email addresses, and company names.
- Use OpenAI Structured Outputs.
- Define a JSON Schema for predictable responses.
- Convert model output into Python dictionaries.
- Handle missing information using `null`.
- Test the extractor with different text inputs.

## Key Concepts Learned

| Concept | Description |
|---|---|
| JSON | Standard format for structured data |
| `json.loads()` | Converts JSON text into Python objects |
| `json.dumps()` | Converts Python objects into JSON text |
| JSON Schema | Defines the expected data structure |
| Structured Outputs | Constrains model responses to a supplied schema |
| `strict=True` | Enforces supported schema constraints |

## Learning Outcome

By completing Day 09, I learned how to:

- Work with JSON in Python.
- Request structured responses from an LLM.
- Define and use JSON Schemas.
- Parse AI-generated JSON into Python dictionaries.
- Build a reusable contact information extraction function.
- Handle missing information and basic response errors.

## GitHub Commit

```bash
git add Day_09/
git commit -m "Complete Day 9 structured outputs and JSON"
git push
```

**Day 09 Status:** Structured Outputs and JSON Practice