# Day 07 — LLM Fundamentals: Mini Project

## Objective

Bring together the concepts learned during Week 1 by building a simple Python simulation of the basic LLM text-generation process.

## Topics Covered

- Basic tokenization
- Converting tokens into numerical IDs
- Vocabulary and unknown tokens
- Next-token prediction
- Autoregressive text generation
- Temperature and probability distribution
- The basic LLM generation pipeline

## Tools and Technologies

- Python
- Jupyter Notebook
- `random` module

## Project Structure

```text
Day_07/
├── 07_llm_fundamentals_lab.ipynb
└── README.md
```

## Hands-on Project — LLM Fundamentals Lab

Built a simplified Python program demonstrating several stages of text generation.

The project includes:

1. A basic tokenizer that splits text into tokens.
2. A vocabulary dictionary that maps tokens to IDs.
3. A next-token prediction simulator using predefined probabilities.
4. An autoregressive text-generation function.
5. A temperature function that adjusts token probabilities.

## Key Concepts

| Concept | Explanation |
|---|---|
| Tokenization | Splits text into smaller units called tokens |
| Token IDs | Numerical identifiers assigned to tokens |
| Embeddings | Numerical vector representations of tokens |
| Transformer | Processes context and relationships between tokens |
| Next-token prediction | Predicts a likely next token |
| Autoregressive generation | Generates tokens iteratively using preceding context |
| Temperature | Controls the randomness of token selection |

## LLM Generation Pipeline

```text
Input Text
    ↓
Tokenization
    ↓
Token IDs
    ↓
Embeddings
    ↓
Transformer Processing
    ↓
Next-Token Prediction
    ↓
Autoregressive Generation
    ↓
Final Response
```

## Important Note

This project is an educational simulation, not a real LLM.

It uses manually defined probabilities and Python's random selection to demonstrate the basic ideas behind token generation.

Real LLMs use trained neural networks to calculate next-token probability distributions.

## Learning Outcome

Understood how the basic stages of LLM text generation fit together, from tokenization and numerical representation to next-token prediction and autoregressive generation.

This project consolidates the fundamental concepts covered during Week 1 of the AI Engineering bootcamp.