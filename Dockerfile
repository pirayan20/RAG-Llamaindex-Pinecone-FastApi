FROM python:3.10-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy project files
COPY pyproject.toml poetry.lock ./
COPY . ./app/

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy environment variables
COPY .env ./

# Expose the port the app runs on
EXPOSE 8501

# Command to run the Streamlit application
CMD ["poetry", "run", "streamlit", "run", "app/app/stream_lit.py", "--server.port=8501", "--server.address=0.0.0.0"]
