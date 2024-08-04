import os
from pinecone import Pinecone, ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore
from scripts.config import app_config

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


def create_index(index_name: str, dimensions: int):
    pc.create_index(
        name=index_name,
        dimension=dimensions,
        metric=app_config.pinecone.metrics,
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )


def get_vector_store(index_name: str) -> PineconeVectorStore:
    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(pinecone_index=index)
    return vector_store


def main():
    create_index(app_config.pinecone.index, app_config.pinecone.dimensions)


if __name__ == "__main__":
    main()
