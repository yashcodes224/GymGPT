from fastapi import FastAPI
from routes.query import router as query_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to GymGPT"}

app.include_router(query_router, prefix="/api")
