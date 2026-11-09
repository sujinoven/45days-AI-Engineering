# Day 29 – Introduction to LLM Evaluation

## Objective

Understand how to evaluate LLM applications systematically and build a basic evaluation harness for a RAG application using Python.

The project demonstrates how to create test datasets, measure keyword coverage, calculate pass rates, track latency, and export evaluation results.

## Topics Covered

- Introduction to LLM evaluation
- Offline evaluation vs online monitoring
- Observability fundamentals
- Evaluation datasets and test cases
- Expected answers and expected keywords
- Keyword coverage
- Evaluation harnesses
- Pass rates and average scores
- Latency measurement
- CSV result logging
- Limitations of keyword-based evaluation

## Tools and Libraries

- Python
- Jupyter Notebook
- `json`
- `re`
- `time`
- `csv`

## Project Structure

```text
Day_29/
├── 29_rag_evaluation.ipynb
├── eval_dataset.json
├── evaluation_results.csv
└── README.md
```

## 1. Creating an Evaluation Dataset

Created a dataset containing test questions, expected answers, and expected keywords.

Started with five RAG-related questions covering retrieval, embeddings, vector databases, chunking, and semantic search.

## 2. Implementing Keyword Coverage

Created `normalize_text()` and `calculate_keyword_coverage()`.

The metric measures the proportion of expected keywords found in a generated answer.

## 3. Building an Evaluation Harness

Created `run_evaluation()` to:

- Execute an answer function for each test question.
- Calculate keyword coverage.
- Determine whether each test passes.
- Measure response latency.
- Capture errors.
- Store individual evaluation results.

## 4. Calculating Evaluation Metrics

Created `summarize_results()` to calculate:

- Total tests
- Passed tests
- Failed tests
- Pass rate
- Average keyword coverage
- Average latency

## 5. Logging Evaluation Results

Exported evaluation records to `evaluation_results.csv` for inspection and comparison.

## 6. RAG Integration

Prepared an adapter to connect the evaluation harness to the Day 21 `chat_with_documents()` application when available.

## Key Learning

LLM applications must be measured rather than judged only by a few successful demonstrations.

A repeatable evaluation dataset and harness provide a foundation for identifying failures and measuring improvements.

Keyword coverage is a basic heuristic, not a complete measure of answer correctness or faithfulness.

## Next Step

**Day 30 – LLM-as-Judge and Advanced Evaluation**

Learn how to use an LLM with a defined evaluation rubric to assess answer quality beyond simple keyword matching.
