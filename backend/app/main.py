
from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(title="Education Support Chatbot")

app.include_router(chat_router)

@app.get("/")
def health_check():
    return {"status": "running"}
