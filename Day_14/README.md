# Day 14 – Week 2 Integration Project

## Project: AI-Powered Contact Extractor CLI

### Objective
Build a command-line AI application that extracts contact information from unstructured text and uses a Python tool to count words.

This project combines the main concepts learned during Week 2.

### Concepts Covered
- Prompt Engineering
- OpenAI Responses API
- Structured Outputs using JSON Schema
- Function Calling and Tool Execution
- Python Functions
- JSON Parsing
- Command-Line Applications
- Error Handling

### Project Structure

```text
Day_14/
├── 14_week2_integration.ipynb
├── week2_contact_tool.py
└── README.md
```

### Features

1. Accepts multiline text from the user.
2. Extracts contact information:
   - Name
   - Email
   - Company
3. Uses structured outputs to return valid JSON.
4. Uses a Python function to count words.
5. Combines the extracted information and word count into one result.
6. Displays the result in formatted JSON.
7. Handles empty input and application errors.

### Example Input

```text
Hi, I'm Sujin. I work at Meta.
Email: sujin@example.com
END
```

Type `END` on a separate line to finish entering text.

### Expected Output Structure

```json
{
    "contact": {
        "name": "Sujin",
        "email": "sujin@example.com",
        "company": "Meta"
    },
    "word_count": 9
}
```

*The actual word count depends on the input text and the counting logic.*

### How to Run

1. Activate your virtual environment.
2. Install the required packages if they are not already installed:

```bash
pip install openai python-dotenv
```

3. Make sure your OpenAI API key is configured in your `.env` file.
4. Run the application from the repository root:

```bash
python Day_14/week2_contact_tool.py
```

### Important Learning

- `extract_contact()` extracts structured information using the OpenAI API.
- `count_words()` performs word counting using Python.
- `get_word_count()` connects the model's tool request to Python execution.
- `process_text()` combines the application results.
- `main()` handles user input and displays the final output.

### Week 2 Outcome

By completing this project, I practiced connecting an LLM to Python functions, generating structured JSON, handling user input, and building a small AI-powered command-line application.
