import time
from fastapi import FastAPI, Request
from app.data_models import QueryRequest, QueryResponse
from app.utils import init_engine

app = FastAPI()
query_engine = init_engine('myproject')

@app.middleware("timing")
async def add_response_timing_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    response.headers["Response-Time"] = str((end_time - start_time) * 1000)
    return response

@app.post("/query")
async def query(request: QueryRequest) -> QueryResponse:
    response = await query_engine.aquery(request.query)
    return QueryResponse(message=response.response)

@app.get("/ping")
async def ping():
    return {"message": "pong"}