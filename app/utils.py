import os
from pinecone import Pinecone
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import VectorStoreIndex, ServiceContext
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

Settings.llm = OpenAI(model='gpt-4o-mini', temperature=0)
Settings.embed_model = OpenAIEmbedding(
    model='text-embedding-3-large', dimensions=1024
)
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

def init_index(index_name: str) -> VectorStoreIndex:
    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(pinecone_index=index)
    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store
    )
    return index

def init_engine(index_name: str):
    index = init_index(index_name)
    query_engine = index.as_query_engine()
    return query_engine

