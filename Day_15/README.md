# Day 15 — Introduction to RAG

## Objective
Understand Retrieval-Augmented Generation (RAG) and build a basic keyword-based document search system.

## Topics Covered
- What RAG means and why it is useful
- Difference between a normal LLM and an LLM connected to external documents
- The five stages of a RAG pipeline:
  1. Ingest documents
  2. Convert text into embeddings
  3. Store vectors
  4. Retrieve relevant content
  5. Generate an answer using retrieved content
- Basic keyword-based document retrieval
- Text cleaning and punctuation removal
- Stop words and their effect on search relevance

## Practical Work
Created a simple Python search function that:
- Accepts a query and a collection of documents
- Cleans punctuation and converts text to lowercase
- Removes common stop words
- Scores documents based on matching words
- Sorts results by relevance score

## Key Learning
Keyword search finds matching words, but it cannot reliably identify similar meanings when different words are used. Embeddings help address this limitation by representing text as numerical vectors.

## Files
- `15_introduction_to_rag.ipynb` — Day 15 learning notebook

## Next Step
Day 16 — Learn text embeddings and vector similarity to find documents based on meaning rather than exact word matches.