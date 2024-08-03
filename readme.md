# RAG-Llamaindex-Pinecone-FastApi

## Overview
This repository contains a Retriever-Reader project that integrates a Llama-index, Pinecone, and FastAPI. The project is designed to handle .pdf file ingestion, indexing, and querying through a user-friendly API.

## Prerequisites
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

## Installation

Clone the repository and install the dependencies using Poetry:

```bash
poetry install
```

## Project Structure

- **scripts/**: Contains scripts for data ingestion and indexing.
  - `ingestion_pipeline.py`: Upserts .pdf files into Pinecone.
  - `create_index.py`: Creates an index in Pinecone.
  - LlamaParse is used for parsing .pdf files within these scripts.

- **app/**: Contains the FastAPI application.
  - `main.py`: The main entry point for the FastAPI server.
  - `./docker-entrypoint.sh`: Script to start the FastAPI application.

## Running the Application
To run the FastAPI application, execute the following script from the root of the project:
```bash
./app/docker-entrypoint.sh
```
This will start the FastAPI server. You can then access the API documentation and interact with the API through the following URL:
```bash
http://localhost:8080/docs
```

## Interacting with the API
Visit `http://localhost:8080/docs` in your web browser to see the Swagger UI where you can send requests to the API and see the responses in real-time. This interface provides a user-friendly way to interact with the various API endpoints created in `main.py`.

