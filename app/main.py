from fastapi import FastAPI
from app.routers.templates_router import router as templates_router

app = FastAPI()
app.include_router(templates_router, prefix="/templates")
