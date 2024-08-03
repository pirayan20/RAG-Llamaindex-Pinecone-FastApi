import os
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.embeddings.openai import OpenAIEmbedding
from scripts.create_index import get_vector_store

embed_model = OpenAIEmbedding(
    model='text-embedding-3-large', 
    dimensions=1024
)

parsing_instruction = """your parsing instruction"""

def process_pdf():
    parser = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
        parsing_instruction=parsing_instruction,
        result_type="text",
    )
    file_extractor = {".pdf": parser}
    reader = SimpleDirectoryReader("./scripts/documents", file_extractor=file_extractor)
    documents = reader.load_data()

    return documents

documents = process_pdf()
vector_store = get_vector_store('myproject')

pipeline = IngestionPipeline(
	transformations=[
		embed_model
	],
    vector_store=vector_store
)

nodes = pipeline.run(documents=documents)