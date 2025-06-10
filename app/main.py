import time
import re
from fastapi import FastAPI, Request, HTTPException
from app.data_models import QueryRequest, QueryResponse
from app.utils import init_engine
from app.config import app_config
from app.log import log_request

app = FastAPI()
query_engine = init_engine(app_config.pinecone.index)


def sanitize_query(query: str) -> str:
    """Perform minimal validation against common SQL injection patterns."""
    injection_regex = re.compile(r"(;|--|/\*|\*/|\b(drop|delete|insert|update|alter)\b)", re.IGNORECASE)
    if injection_regex.search(query):
        raise HTTPException(status_code=400, detail="Invalid characters in query")
    return query


# Add a middleware to measure HTTP response time
@app.middleware("http")
async def add_response_timing_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    response.headers["Response-Time"] = str((end_time - start_time) * 1000)
    return response


@app.post("/query")
async def query(request: QueryRequest) -> QueryResponse:
    sanitized = sanitize_query(request.query)
    log_request(sanitized)
    response = await query_engine.aquery(sanitized)
    return QueryResponse(message=response.response)


@app.get("/ping")
async def ping():
    return {"message": "pong"}
