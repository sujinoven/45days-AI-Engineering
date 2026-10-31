# Day 03 — Tokenization and Subword Tokenizers

## Objective
Understand how text is converted into tokens and numerical IDs before being processed by Large Language Models (LLMs).

## Topics Covered
- Characters, words and tokens
- Why LLMs use tokenization
- Word-based tokenization using Python regular expressions
- Converting tokens into numerical token IDs
- Handling unknown words using `<UNK>`
- Subword tokenization
- Longest-match-first tokenization
- Real-world tokenization using `tiktoken`
- Introduction to Byte Pair Encoding (BPE)
- Token embeddings and the LLM processing pipeline

## Practical Exercises

### 1. Basic Word Tokenizer
Built a Python tokenizer using `re.findall()` to split text into words and punctuation.

### 2. Token IDs
Created a vocabulary dictionary and converted tokens into numerical IDs.

### 3. Unknown Token Handling
Introduced `<UNK>` to handle words that are not present in the vocabulary.

### 4. Subword Tokenizer
Implemented a simple longest-match-first tokenizer using a manually defined vocabulary.

Examples:
- `playing` → `play` + `ing`
- `unhappy` → `un` + `happy`
- `player` → `play` + `er`
- `python` → `py` + `thon`

### 5. Real LLM Tokenizer
Used the `tiktoken` Python library to:
- Load the `cl100k_base` encoding
- Convert text into token IDs
- Count tokens
- Decode token IDs back into text

### 6. Byte Pair Encoding (BPE)
Implemented a simplified BPE algorithm to:
- Split words into individual characters
- Count adjacent character pairs
- Identify the most frequent pair
- Merge adjacent pairs
- Repeat the merging process
- Inspect the learned merge rules

## LLM Processing Pipeline

Studied the simplified process:

```text
Input Text
    ↓
Tokenizer
    ↓
Token IDs
    ↓
Embedding Layer
    ↓
Transformer Model
    ↓
Predicted Token IDs
    ↓
Decoded Text
```

## Key Concepts Learned
- Tokens are not always complete words.
- Token IDs are numerical identifiers for tokens.
- `<UNK>` represents an unknown token in a vocabulary.
- Subword tokenization helps represent unfamiliar words using smaller pieces.
- Embeddings map token IDs to learned numerical vectors.
- BPE builds subword vocabularies by repeatedly merging frequent adjacent pairs.
- Tokenization is an essential preprocessing step for LLMs.

## Important Notes
- The longest-match-first tokenizer is an educational implementation using a manually defined vocabulary.
- The BPE implementation demonstrates the basic merging concept and is not a production-grade tokenizer.
- `tiktoken` provides access to real tokenizer encodings,