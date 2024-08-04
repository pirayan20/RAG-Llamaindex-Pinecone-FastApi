from pydantic import BaseModel
import yaml
import os

class PineconeConfig(BaseModel):
    index: str
    dimensions: int
    metrics: str

class EmbedModelConfig(BaseModel):
    name: str

class PromptConfig(BaseModel):
    parsing_instruction: str
    parse_type: str

class AppConfig(BaseModel):
    pinecone: PineconeConfig
    embedmodel: EmbedModelConfig
    prompts: PromptConfig

config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
with open(config_path, 'r') as f:
    config_data = yaml.load(f, Loader=yaml.FullLoader)
app_config = AppConfig(**config_data)
