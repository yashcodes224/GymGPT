from fastapi import APIRouter

router = APIRouter()

@router.post("/query")
async def handle_query(query: str):
    return {"response": f"Your query was: {query}"}
