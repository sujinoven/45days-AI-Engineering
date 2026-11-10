# Day 34 — Deployment Basics: Turning an LLM Notebook into a Reusable API

## Objective

Learn how to convert an LLM application into a reusable HTTP API using FastAPI and Uvicorn.

## Topics Covered

- Introduction to API deployment
- FastAPI fundamentals
- HTTP GET and POST endpoints
- Request validation with Pydantic
- Connecting an LLM to an API
- Running an API using Uvicorn
- Testing APIs with Swagger UI
- Calling APIs using Python requests
- Environment variables and API key security
- Basic deployment and production considerations

## Project Structure

```text
Day_34/
├── 34_llm_api_deployment.ipynb
├── app.py
├── requirements.txt
└── README.md
```

## Application Features

- Created a FastAPI application.
- Built a reusable `generate_answer()` function.
- Connected the OpenAI Responses API.
- Created a GET `/` health endpoint.
- Created a POST `/ask` endpoint.
- Validated incoming questions using Pydantic.
- Returned AI-generated answers as JSON.
- Ran the application using Uvicorn.
- Tested the application using Swagger UI.
- Called the API using Python requests.

## Tools and Libraries

- Python
- Jupyter Notebook
- FastAPI
- Uvicorn
- OpenAI Python SDK
- python-dotenv
- Pydantic
- requests

## Important Concepts

- FastAPI builds HTTP APIs.
- Uvicorn runs the application server.
- Endpoints define the operations an API supports.
- POST requests can send data to an API.
- Pydantic validates incoming request data.
- JSON is used to exchange data between applications.
- API keys should be stored securely in environment variables.
- Local development is different from production deployment.

## Run the Application

Start the server from the Day_34 folder:

```bash
uvicorn app:app --reload
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Git Commands

```bash
git add Day_34/
git commit -m "Complete Day 34 LLM API deployment"
git push
```

## Key Takeaway

Deployment makes an LLM application accessible to other programs through an API. FastAPI provides the interface, Uvicorn runs the server, and the LLM function handles AI generation.

This is a foundation for deploying production AI applications. Production systems also require authentication, rate limiting, monitoring, secure configuration and reliable hosting.
