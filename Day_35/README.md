# Day 35 — LLMOps Evaluation & Monitoring Capstone

## Objective

Build a small LLMOps pipeline that combines prompt management, evaluation, observability, experiment tracking and reporting.

## Topics Covered

- LLMOps workflow
- Prompt version management
- Evaluation datasets
- LLM answer generation
- Keyword coverage evaluation
- Request logging
- Latency tracking
- Token usage monitoring
- Experiment summaries
- JSON and CSV reporting
- Prompt comparison

## Notebook

`35_llmops_capstone.ipynb`

## Project Structure

```text
Day_35/
├── 35_llmops_capstone.ipynb
├── prompts/
│   └── prompts.json
├── datasets/
│   └── test_cases.json
├── results/
│   ├── evaluation_results.json
│   ├── evaluation_results.csv
│   └── pipeline.log
└── README.md
```

## Practical Work

- Created a prompt registry with two versions.
- Created a fixed evaluation dataset.
- Built an LLM answer-generation function.
- Implemented keyword coverage evaluation.
- Added request IDs and application logging.
- Recorded latency and token usage.
- Built a complete evaluation pipeline.
- Calculated pass rates and average scores.
- Saved experiment results in JSON and CSV.
- Compared prompt versions.

## Important Lessons

- LLM applications need continuous evaluation and monitoring.
- Fixed datasets make prompt comparisons more meaningful.
- Logs and request IDs help diagnose failures.
- Latency and token usage are important operational metrics.
- Experiment reports preserve useful evidence.
- Keyword coverage is a basic heuristic, not a complete measure of correctness.
- Production systems require stronger quality checks, privacy controls and failure handling.

## Tools

- Python
- Jupyter Notebook
- OpenAI Python SDK
- python-dotenv
- Pandas
- JSON
- Logging

## Git Commands

```bash
git add Day_35/
git commit -m "Complete Day 35 LLMOps evaluation capstone"
git push
```

## Key Takeaway

LLMOps brings evaluation, observability and experiment tracking together. A reliable AI application must not only generate answers, but also measure quality, record performance and provide evidence that changes improve the system.
