from fastapi import APIRouter, UploadFile, File
from ml.predict import classify_document
from nlp.preprocessing import extract_text

router = APIRouter()

@router.post("/classify")
async def classify(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)
    label = classify_document(text)
    return {"label": label}
