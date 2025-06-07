FROM python:3.10-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy poetry configuration files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the application code
COPY app/ ./app/

# Copy the documents directory to the expected location
COPY scripts/documents/ ./app/scripts/documents/

# Copy environment variables
COPY .env ./

# Expose the port the app runs on
EXPOSE 8501

# Command to run the Streamlit application
CMD ["poetry", "run", "streamlit", "run", "app/stream_lit.py", "--server.port=8501", "--server.address=0.0.0.0"]
