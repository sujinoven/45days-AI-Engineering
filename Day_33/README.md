# Day 33 — LLMOps: Prompt Versioning and Experiment Tracking

## Objective

Learn how to manage prompt versions, run controlled LLM experiments, compare results and maintain reproducibility.

## Topics Covered

- Introduction to LLMOps
- Prompt versioning
- Prompt registries
- JSON-based prompt storage
- Fixed evaluation datasets
- Experiment tracking
- Prompt comparison
- Reproducibility
- Prompt promotion and rollback
- Introduction to MLflow, LangSmith and Weights & Biases

## Notebook

`33_llmops_prompt_versioning.ipynb`

## Project Structure

```text
Day_33/
├── 33_llmops_prompt_versioning.ipynb
├── prompts/
│   └── prompt_versions.json
├── experiments/
│   ├── test_cases.json
│   └── experiment_results.json
└── README.md
```

## Important Lessons

- Prompt changes should be version-controlled.
- Experiments should use consistent evaluation datasets.
- Prompt quality should be measured rather than assumed.
- Experiment tracking records settings and results.
- Reproducibility requires preserving prompt text, model information and datasets.
- Rollback helps recover from prompt regressions.
- Keyword coverage is a basic heuristic, not a complete measure of answer quality.

## Tools

- Python
- Jupyter Notebook
- OpenAI Python SDK
- python-dotenv
- JSON
- MLflow (optional)
- LangSmith (optional)
- Weights & Biases (optional)

##

## Git Commands

```bash
git add Day_33/
git commit -m "Complete Day 33 LLMOps prompt versioning"
git push
```

## Key Takeaway

LLMOps makes AI applications easier to test, maintain and improve. Prompt versioning and experiment tracking help developers understand what changed, measure its impact and safely roll back when necessary.
