from fastapi import FastAPI

app = FastAPI(title="Love-as-a-Service")

@app.get("/")
async def root():
    return {
        "message": "Love-as-a-Service API"
    }