from fastapi import FastAPI
from backend.route.query import get_answer

app = FastAPI()

@app.post("/query")
async def query(request: dict):
    query = request['query']
    answer = get_answer(query)
    return {"answer": answer}
