import os
from pinecone import Pinecone
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from app.config import app_config

Settings.llm = OpenAI(model=app_config.models.main_llm, temperature=0)
Settings.embed_model = OpenAIEmbedding(
    model=app_config.models.openai_embeddings, dimensions=app_config.models.dimensions
)
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


def init_index(index_name: str) -> VectorStoreIndex:
    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(pinecone_index=index)
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    return index


def init_engine(index_name: str):
    index = init_index(index_name)
    query_engine = index.as_query_engine()
    return query_engine
