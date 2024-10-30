from fastapi import APIRouter

router = APIRouter(prefix='/check', tags=['CHECK'])

@router.get("/", summary="Health check for the API")
async def check():
    return {"status": "Its working properly!"}