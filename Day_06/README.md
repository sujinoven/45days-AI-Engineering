# Day 06 — How an LLM Generates an Answer

## Objective

Understand how a Large Language Model (LLM) generates text by predicting one token at a time.

## Topics Covered

- The LLM generation pipeline
- Tokenization and token IDs
- Embeddings and transformers
- Next-token prediction
- Autoregressive text generation
- How generated tokens become part of the context

## Tools and Technologies

- Python
- Jupyter Notebook
- `random` module

## Project Structure

```text
Day_06/
├── 06_next_token_generation.ipynb
└── README.md
```

## Hands-on Project — Next-Token Generation Simulator

Built a simple Python program to simulate how an LLM generates text.

The program:

1. Defines possible next tokens and their probabilities.
2. Predicts the next token using `random.choices()`.
3. Adds the generated token to the existing sequence.
4. Repeats the process until an end token or token limit is reached.

## Example Output

```text
Artificial intelligence can learn from data today

Artificial intelligence can help people solve problems today

Artificial intelligence can reason about problems today
```

The output may vary because the simulator uses probability-based random selection.

## Key Concepts

| Concept | Explanation |
|---|---|
| Tokenization | Converts text into tokens |
| Embeddings | Represents tokens as numerical vectors |
| Transformer | Processes context and relationships between tokens |
| Next-token prediction | Predicts a likely next token |
| Autoregressive generation | Generates tokens using previously generated context |

## Important Note

This project is an educational simulation. It uses manually defined probabilities and Python's random selection. It is **not a real LLM or trained neural network**.

Real LLMs use trained neural-network parameters to calculate next-token probability distributions.

## Learning Outcome

Understood the basic process behind LLM text generation, including next-token prediction and autoregressive generation.

