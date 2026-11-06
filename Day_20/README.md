# Day 20 – Loading PDF and Markdown Documents into RAG

## Objective

Learn how to load real-world PDF and Markdown documents, extract their text, split the content into smaller chunks, generate embeddings, and store the chunks in ChromaDB with source metadata.

## Topics Covered

- Document ingestion in RAG
- Loading Markdown files using Python
- Extracting PDF text using `pypdf`
- Reading PDF content page by page
- Document chunking
- Chunk overlap
- Preserving source information with metadata
- Generating embeddings using OpenAI
- Storing document chunks in ChromaDB
- Semantic retrieval with source information

## Tools and Libraries

- Python
- Jupyter Notebook
- OpenAI API
- `pypdf`
- `chromadb`
- `python-dotenv`
- `pathlib`

## Project Structure

```text
Day_20/
├── documents/
│   ├── ai_notes.md
│   └── sample_notes.pdf
├── chroma_db/
├── 20_document_ingestion.ipynb
└── README.md
```

## 1. Markdown Document Loading

Used Python's `pathlib` and `open()` to load Markdown files and extract their text.

## 2. PDF Text Extraction

Used `PdfReader` from `pypdf` to:

- Open PDF documents
- Read pages individually
- Extract text from each page
- Preserve page numbers for source tracking

Note: Scanned PDFs may require OCR because `pypdf` generally extracts selectable text rather than text embedded in page images.

## 3. Document Chunking

Split long documents into smaller chunks.

Implemented:

- Fixed-size chunking
- Overlapping chunks

Chunk overlap helps preserve context between adjacent chunks.

## 4. Source Metadata

Attached metadata to document chunks, including:

- Source filename
- PDF page number
- Chunk number
- File type

This makes it possible to trace retrieved information back to its original document.

## 5. Embedding Generation

Generated embeddings using the OpenAI model:

`text-embedding-3-small`

Converted document chunks into numerical vectors for semantic retrieval.

## 6. ChromaDB Storage

Used a persistent ChromaDB collection to store:

- Document chunks
- Embeddings
- Unique document IDs
- Source metadata

Used `collection.upsert()` to insert or update records.

## 7. Semantic Retrieval

Generated an embedding for a question and searched ChromaDB using:

`collection.query()`

Retrieved the top 3 relevant document chunks and displayed their source filenames and page numbers.

## Key Learning

A RAG system needs more than an LLM and embeddings. It also needs a reliable document ingestion process.

The pipeline practiced today:

**Documents → Text Extraction → Chunking → Embeddings → ChromaDB → Retrieval**

Preserving source metadata is important because it helps the system identify where retrieved information originated.

## Next Step

**Day 21 – RAG Integration Project**

Build on document ingestion, embeddings, ChromaDB retrieval, and answer generation to create a chat-with-your-documents application.
