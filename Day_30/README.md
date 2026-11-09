# Day 30 – LLM-as-Judge and Advanced Evaluation

## Objective

Understand how to use an LLM as an evaluator for AI-generated answers.

Built a structured evaluation system using the OpenAI Responses API to assess correctness, relevance, and faithfulness.

## Topics Covered

- LLM-as-Judge
- Evaluation rubrics
- Correctness
- Relevance
- Faithfulness
- Structured Outputs
- JSON Schema
- Batch evaluation
- Aggregate evaluation metrics
- Human calibration
- Judge reliability and limitations

## Tools and Libraries

- Python
- Jupyter Notebook
- OpenAI API
- `openai`
- `python-dotenv`
- `json`

## Project Structure

```text
Day_30/
├── 30_llm_as_judge.ipynb
├── eval_dataset.json
├── llm_judge_results.json
└── README.md
```

## 1. Evaluation Dataset

Created test cases containing:

- Unique test IDs
- Questions
- Retrieved context
- Reference answers
- Generated answers

Included deliberately incorrect answers to test judge behavior.

## 2. Evaluation Rubric

Defined a structured rubric with three dimensions:

- Correctness – whether the answer communicates accurate information.
- Relevance – whether it directly addresses the question.
- Faithfulness – whether claims are supported by retrieved context.

## 3. Structured Judge Output

Created a JSON Schema containing evaluation scores, an overall score, a pass/fail result, and an explanation.

Used the OpenAI Responses API with structured output to obtain machine-readable evaluations.

## 4. LLM Judge Function

Implemented `evaluate_answer()` to:

- Prepare evaluation input.
- Send the question, context, reference, and generated answer to the judge.
- Request structured JSON output.
- Parse the response.
- Validate score ranges.

## 5. Batch Evaluation

Created `evaluate_dataset()` to evaluate multiple test cases.

Stored the individual results for later analysis.

## 6. Evaluation Metrics

Created `summarize_judge_results()` to calculate:

- Average correctness
- Average relevance
- Average faithfulness
- Average overall score
- Pass rate
- Failed test count

## 7. Saving Results

Exported the structured evaluation results to `llm_judge_results.json`.

## Key Learning

LLM-as-Judge can evaluate answer quality beyond simple keyword matching.

However, an LLM judge is not ground truth. Its decisions should be tested against human judgments, and its rubric and outputs should be inspected.

## Next Step

**Day 31 – RAG Evaluation Metrics**

Explore retrieval quality, context precision, context recall, answer relevance, and faithfulness using more systematic evaluation methods.
