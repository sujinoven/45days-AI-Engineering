# Day 04 — Understanding Large Language Models

## Objective
Understand how Large Language Models (LLMs) are trained, how they generate responses, and why they sometimes produce incorrect information.

## Topics Covered
- Pretraining
- Post-training
- Supervised fine-tuning (SFT)
- Preference optimization
- Inference
- Next-token prediction
- Autoregressive text generation
- Context windows
- LLM hallucinations
- Techniques to reduce hallucinations

## Practical Exercise

### 1. Next-Token Prediction Simulation
Built a simple Python simulation using a manually defined next-token probability table.

The simulation demonstrates:
- Predicting the next token
- Selecting tokens using probability-based sampling
- Generating text one token at a time
- Repeating predictions until a stopping condition is reached

### 2. LLM Lifecycle

Studied the three broad stages:

1. **Pretraining:** Learning language patterns from large amounts of data.
2. **Post-training:** Adapting the pretrained model to follow instructions and produce useful responses.
3. **Inference:** Using the trained model to generate responses.

### 3. Context Windows
Learned how context windows limit the amount of tokenized input and generated output a model can process.

### 4. Hallucinations
Studied why LLMs can generate false or unsupported information and how retrieval, validation, and evaluation can help reduce this risk.

## Key Concepts Learned
- LLMs commonly use next-token prediction.
- Autoregressive models generate tokens sequentially.
- Pretraining and post-training serve different purposes.
- Inference is the process of using a trained model.
- Temperature influences token selection during generation.
- Context windows limit available processing context.
- RAG can provide relevant information to help reduce hallucinations.

## Important Note
The next-token prediction exercise is an educational simulation using manually assigned probabilities. It is not a real neural network or LLM.

## Project Structure

```text
Day_04/
├── 04_llm_lifecycle.ipynb
└── README.md
```

## How to Run
1. Open `04_llm_lifecycle.ipynb` in Jupyter Notebook.
2. Select the Python environment used for the AI Engineering bootcamp.
3. Run the notebook cells in order.
4. Inspect the generated text and experiment with multiple runs.

## Outcome
Understood the basic LLM lifecycle, next-token prediction, autoregressive generation, context windows, and hallucinations. Built a small Python simulation to demonstrate text generation.