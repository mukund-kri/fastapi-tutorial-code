from datetime import datetime

from fastapi import APIRouter


# Create a router on which the time related endpoints are specified
router = APIRouter(
    prefix="/time",
    responses={404: {"description": "Not found"}},
)


# Define the endpoint
@router.get("/")
async def get_time():
    now = datetime.now()
    return {"time": now.isoformat()}


# Path: time/year
@router.get("/year")
async def get_year():
    now = datetime.now()
    return {"year": now.year}
