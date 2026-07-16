from fastapi import FastAPI
from app.api.routes.chat import router as chat_router
app = FastAPI(
    title="SAKURA",
    version="0.1.0"
)
app.include_router(chat_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to SAKURA AI Operating System"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }

@app.get("/version")
async def version():
    return {
        "version": "0.1.0"
    }