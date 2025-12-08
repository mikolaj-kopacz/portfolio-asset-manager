from fastapi import FastAPI


app = FastAPI(title="Asset Manager A", version="1.0.0")


@app.get("/")
async def root_message():
    return {"message": " Welcome to Asset Manager API","status":"running"}

