# Day 17 — Document Chunking Strategies

## Objective
Understand how large documents are divided into smaller chunks for better information retrieval in RAG applications.

## Topics Covered
- What document chunking is
- Why chunking is important in RAG
- Fixed-size chunking
- Chunking with overlap
- Sentence-based chunking
- Chunk size and overlap
- Preserving context across chunk boundaries

## Practical Work

### 1. Fixed-Size Chunking
Created a Python function that splits a document into chunks based on a specified character count.

### 2. Overlapping Chunking
Implemented overlapping chunks to preserve some context between consecutive chunks.

### 3. Sentence-Based Chunking
Created a function that splits a document into individual sentences while preserving sentence boundaries.

### 4. Strategy Comparison
Compared the three approaches based on chunk size, context preservation, and sentence boundaries.

## Key Learnings
- Chunking divides large documents into smaller pieces.
- Fixed-size chunking can split sentences.
- Overlap helps preserve context between neighboring chunks.
- Sentence-based chunking keeps complete sentences together, but chunk sizes can vary.
- Choosing an appropriate chunking strategy can improve retrieval quality.

## Files
- `17_document_chunking.ipynb` — Day 17 learning notebook

## Next Step
Day 18 — Vector Databases and ChromaDB: learn how to store document chunks and their embeddings for efficient semantic search in a RAG application.