import logging
import sys
import os
from dotenv import load_dotenv
from app.log import CustomJsonFormatter

load_dotenv()

# Get the environment variable
env = os.getenv("ENVIRONMENT", "local")

# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

if env == "prod":
    handler = logging.StreamHandler(sys.stdout)
    formatter = CustomJsonFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
else:
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)
