# Day 16 — Text Embeddings and Vector Similarity

## Objective
Understand how text embeddings represent the meaning of text and how vector similarity can be used to retrieve relevant documents.

## Topics Covered
- What text embeddings are
- Converting text into numerical vectors
- OpenAI `text-embedding-3-small` model
- Embedding dimensions
- Cosine similarity
- Semantic search
- Similarity scores and thresholds
- Difference between keyword search and semantic search

## Libraries Used
- `openai`
- `numpy`
- `python-dotenv`

## Practical Work

### 1. Generate Text Embeddings
Used the OpenAI embedding API to convert sentences into numerical vectors.

### 2. Embed Multiple Documents
Generated embeddings for a collection of documents and stored them in a Python list.

### 3. Implement Cosine Similarity
Created a Python function using NumPy to calculate the similarity between two vectors.

### 4. Build Semantic Search
- Converted a search query into an embedding.
- Compared the query embedding with document embeddings.
- Calculated similarity scores.
- Ranked documents from highest to lowest similarity.

### 5. Apply a Similarity Threshold
Experimented with filtering out documents whose similarity scores were below a selected threshold.

## Example Results

Query: "How can AI retrieve information from documents?"

| Document | Similarity |
|---|---:|
| RAG combines document retrieval with language generation. | 0.5388 |
| Machine learning allows computers to learn from data. | 0.3935 |
| Neural networks are inspired by the human brain. | 0.2417 |
| Python is a popular programming language. | 0.0668 |

## Key Learnings
- Embeddings represent text as numerical vectors.
- Semantically similar text can have similar embeddings even when the exact words differ.
- Cosine similarity measures the directional similarity between vectors.
- Semantic search ranks documents based on their similarity to a query.
- Similarity scores are not probabilities or percentages of correctness.
- A similarity threshold can help filter less relevant results.

## Files
- `16_text_embeddings.ipynb` — Day 16 learning notebook

## Next Step
Day 17 — Document Chunking Strategies: learn how to split large documents into smaller, useful pieces for better retrieval in a RAG application.