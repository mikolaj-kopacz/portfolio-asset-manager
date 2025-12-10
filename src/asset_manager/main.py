from fastapi import FastAPI
from src.asset_manager.api.router import api_router


app = FastAPI(title="Asset Manager A", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root_message():
    return {"message": " Welcome to Asset Manager API", "status": "running"}
