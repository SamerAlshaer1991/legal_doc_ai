from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="LexiMind - Legal Document Classifier")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to LexiMind Legal AI API"}
