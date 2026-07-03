# IT Support RAG Agent

A Retrieval-Augmented Generation (RAG) agent for IT support, built with Python and Qdrant.

## Setup

### 1. Services & Prerequisites

Before running the agent, you need to start the required backend services.

**Qdrant Database:**
Start the local Qdrant server:
```powershell
.\qdrant.exe
```

**Ollama Server:**
Make sure you have downloaded the required model to your local `./models` directory before proceeding. Then, set the model store environment variable and start the Ollama server:

```powershell
$env:OLLAMA_MODELS = "C:\Users\You\your_project\models"
ollama serve
```

### 2. Virtual Environment

Next, activate the Python virtual environment:

**Windows (PowerShell):**
```powershell
.\it-support\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.\it-support\Scripts\activate.bat
```
## Pipeline

![Hybrid RAG Ingestion Pipeline](./images/pipeline.svg)

The system consists of a two-step pipeline:

### 1. Ingestion
Run the ingestion script to process your markdown documentation, split it into chunks, embed it, and store it in the Qdrant vector database.

```powershell
python .\ingest.py
```

### 2. Retrieval
Run the retrieval script to perform hybrid searches (BM25 + Dense embeddings) with Reciprocal Rank Fusion (RRF) against the ingested chunks.

```powershell
python .\retrieve.py
```
*Note: The retrieval script will wait for standard input when it runs. Type your query and press Enter to search the database.*
