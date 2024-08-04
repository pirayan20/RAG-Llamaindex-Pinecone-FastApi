from pydantic import BaseModel
import yaml
import os


class PineconeConfig(BaseModel):
    index: str


class ModelConfig(BaseModel):
    openai_embeddings: str
    main_llm: str
    dimensions: int


class PromptConfig(BaseModel):
    parsing_instruction: str


class AppConfig(BaseModel):
    pinecone: PineconeConfig
    models: ModelConfig
    verbose: bool


config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(config_path, "r") as f:
    config_data = yaml.load(f, Loader=yaml.FullLoader)
app_config = AppConfig(**config_data)
