# Day 21 – Chat with Your Documents (RAG Project)

## Objective

Build a basic Retrieval-Augmented Generation (RAG) application that allows users to ask questions about PDF and Markdown documents and receive answers grounded in the retrieved document content.

## Topics Covered

- RAG pipeline integration
- PDF and Markdown document ingestion
- PDF text extraction using `pypdf`
- Document chunking and overlap
- Source metadata preservation
- Text embeddings using OpenAI
- Vector storage using ChromaDB
- Semantic search and document retrieval
- Context construction
- Answer generation using the OpenAI Responses API
- Source-aware question answering

## Tools and Libraries

- Python
- Jupyter Notebook
- OpenAI API
- ChromaDB
- pypdf
- python-dotenv
- pathlib

## Project Structure

```text
Day_21/
├── documents/
│   ├── ai_notes.md
│   └── sample_notes.pdf
├── chroma_db/
├── 21_chat_with_documents.ipynb
└── README.md
```

## 1. Document Ingestion

Created `load_documents()` to load documents from a folder.

Supported formats:

- Markdown (`.md`)
- PDF (`.pdf`)

Used `pypdf.PdfReader` to extract PDF text page by page.

Preserved document filenames and PDF page numbers.

## 2. Document Chunking

Created `chunk_documents()` to split long document sections into smaller chunks.

Implemented:

- Fixed-size chunking
- Chunk overlap
- Source metadata preservation

Each chunk retains:

- Source filename
- Page number
- Chunk number

## 3. Embedding Generation

Created `generate_embeddings()` using the OpenAI embedding model:

`text-embedding-3-small`

Converted document chunks into numerical vectors for semantic search.

## 4. ChromaDB Storage

Created a persistent ChromaDB database and collection.

Stored:

- Document chunks
- Embeddings
- Unique IDs
- Source metadata

Used `collection.upsert()` to insert or update records.

## 5. Document Retrieval

Created `retrieve_documents()` to:

1. Convert the user's question into an embedding.
2. Search ChromaDB for relevant passages.
3. Retrieve the top matching chunks.
4. Return document text and source metadata.

## 6. Answer Generation

Created `generate_answer()` using the OpenAI Responses API.

The function:

- Combines retrieved passages into context.
- Includes source filenames and page numbers.
- Sends the context and question to the LLM.
- Instructs the model to answer using only the provided context.
- Asks the model to acknowledge when the documents do not contain enough information.

## 7. Complete RAG Application

Created `chat_with_documents()` to connect retrieval and answer generation.

The complete pipeline:

**PDF / Markdown → Text Extraction → Chunking → Embeddings → ChromaDB → Retrieval → Context → LLM Answer**

## Key Learning

A RAG application combines document retrieval with language generation.

Instead of relying only on the LLM's existing knowledge, the application retrieves relevant passages from external documents and provides them as context for generating an answer.

Source metadata helps trace retrieved information back to its original document and page.

## Week 3 Summary

| Day    | Topic                            |
| ------ | -------------------------------- |
| Day 15 | Introduction to RAG              |
| Day 16 | Embeddings and semantic search   |
| Day 17 | Document chunking                |
| Day 18 | Vector databases and ChromaDB    |
| Day 19 | Generating answers with RAG      |
| Day 20 | PDF and Markdown ingestion       |
| Day 21 | Chat-with-your-documents project |

## Next Step

**Week 4 – AI Agents and Orchestration**

Explore how AI models use tools, make decisions, and coordinate multi-step tasks.
