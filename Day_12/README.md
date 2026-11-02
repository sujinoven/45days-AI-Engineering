# Day 12 – API Error Handling, Retries and Rate Limits

## Objective

Learn how to handle errors in AI applications, manage temporary API failures, and build reliable Python applications using the OpenAI API.

## Topics Covered

- Understanding common API errors
- Authentication errors
- Rate limit errors
- API connection errors
- Invalid request errors
- Python `try` and `except`
- Handling specific exceptions
- Retry mechanisms
- Exponential backoff
- Building reliable AI assistants

## Tools and Technologies

- Python
- Jupyter Notebook
- OpenAI Python SDK
- OpenAI Responses API
- python-dotenv
- time module

## Project Structure

```text
Day_12/
├── 12_api_error_handling.ipynb
└── README.md
```

## Practical Exercises

### 1. Basic Error Handling

Practised Python `try` and `except` to handle API errors without unexpectedly terminating the application.

### 2. Specific API Error Handling

Handled common exceptions:

- `AuthenticationError`
- `RateLimitError`
- `APIConnectionError`
- `BadRequestError`
- `APIStatusError`

### 3. Retry Mechanism

Created a Python function that retries temporary API failures.

Implemented exponential backoff using increasing wait times:

- First retry: 1 second
- Second retry: 2 seconds
- Third retry: 4 seconds

### 4. Mini Project – Reliable AI Assistant

Built a Python AI assistant that:

- Accepts user questions.
- Sends requests to the OpenAI API.
- Retries temporary failures.
- Displays AI-generated responses.
- Handles errors with useful messages.

## Key Concepts Learned

| Concept | Description |
|---|---|
| Exception handling | Managing errors using `try` and `except` |
| Authentication error | Problem with API authentication |
| Rate limit | Request or usage limit reached |
| Retry mechanism | Trying a failed request again |
| Exponential backoff | Increasing the delay between retries |
| Reliable application | An application that handles failures gracefully |

## Important Learning

Not all API errors should be retried.

Temporary connection failures and rate limits may be retryable. Authentication errors and invalid requests usually require fixing the underlying problem.

The OpenAI Python SDK also provides automatic retries for certain temporary errors.

## Learning Outcome

By completing Day 12, I learned how to:

- Identify common API errors.
- Handle exceptions in Python.
- Retry temporary API failures.
- Implement exponential backoff.
- Build a more reliable AI assistant.

## GitHub Commit

```bash
git add Day_12/
git commit -m "Complete Day 12 API error handling and retries"
git push
```

## Resources

- [OpenAI API Error Codes](https://platform.openai.com/docs/guides/error-codes)
- [OpenAI API Documentation](https://platform.openai.com/docs/overview)

---

**Day 12 Status:** Completed after finishing the notebook exercises, mini-project, quiz, and GitHub commit.