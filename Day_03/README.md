# Day 03 — Tokenization and Subword Tokenizers

## Objective
Understand how text is converted into tokens and numerical IDs before being processed by an AI language model.

## Topics Covered
- What are characters, words and tokens?
- Why LLMs use tokenization
- Word-based tokenization using Python regular expressions
- Converting tokens into numerical token IDs
- Handling unknown words using `<UNK>`
- Understanding subword tokenization
- Building a simple longest-match-first subword tokenizer
- Understanding the connection between tokenization and LLMs
- Introduction to Byte Pair Encoding (BPE)

## Practical Exercises

### 1. Basic Tokenizer
Created a Python tokenizer using `re.findall()` to split text into words and punctuation.

### 2. Token IDs
Created a vocabulary dictionary and converted tokens into numerical IDs.

### 3. Unknown Tokens
Introduced `<UNK>` to handle words that are not present in the vocabulary.

### 4. Subword Tokenizer
Built a simple longest-match-first tokenizer that splits words into smaller vocabulary pieces.

Examples:

- `playing` → `play` + `ing`
- `unhappy` → `un` + `happy`
- `python` → `py` + `thon`

### 5. LLM Processing Pipeline
Studied the simplified pipeline:

Text → Tokenizer → Token IDs → Embeddings → Transformer → Output Tokens

## Key Concepts Learned
- Tokens are not always complete words.
- Token IDs are numerical identifiers for tokens.
- Unknown tokens can be represented using `<UNK>`.
- Subword tokenization helps represent unfamiliar words using smaller known pieces.
- Embeddings convert token IDs into learned numerical vectors.
- Real LLM tokenizers use more sophisticated approaches, including BPE.

## Important Note
The subword tokenizer built in this exercise is an educational implementation. It uses a manually defined vocabulary and longest-match-first splitting. It is not a production-grade BPE tokenizer.

## Project Structure

```text
Day_03/
├── 03_tokenization.ipynb
└── README.md
```

## How to Run
1. Open `03_tokenization.ipynb` in Jupyter Notebook.
2. Select the Python environment used for the AI Engineering bootcamp.
3. Run all cells from top to bottom.

## Outcome
Built basic and subword tokenizers, converted text into token IDs, and understood how tokenization prepares text for LLM processing.