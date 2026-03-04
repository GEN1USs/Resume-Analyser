from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from .predict import classify_resume

app = FastAPI(title="Resume Analyzer API")

class JobDescription(BaseModel):
    text: str

@app.post("/analyze/")
async def analyze_resume(job: JobDescription, resume: UploadFile = File(...)):
    content = (await resume.read()).decode("utf-8", errors="ignore")
    label, score = classify_resume(content + " " + job.text)
    return {"prediction": label, "confidence": score}