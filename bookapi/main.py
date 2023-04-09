from fastapi import FastAPI

from api import time, books

# Initialize the FastAPI app
app = FastAPI()

# Include the external routers
app.include_router(time.router)
app.include_router(books.router)
