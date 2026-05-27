from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
import random 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "https://beatrizneves1403.github.io"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisResult(BaseModel):
    filename: str
    is_ai_generated: bool
    confidence: float
    label: str

@app.get("/health")
def health():
    return {"status": "ok", "mode": "mock"}

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_image(file: UploadFile = File(...), force_result: str = None):
    allowed_types = ["image/jpeg", "image/png", "image/webp"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo nao suportado: {file.content_type}. Use JPG, PNG ou WEBP. "
        )
    contents = await file.read() 
    if len(contents) > 5 * 1024 * 1024: 
        raise HTTPException(
            status_code=400,
            detail="Arquivo muito grande. Tamanho maximo permitido: 5MB."
        )

    #Mock — resultado inventado. No futuro vira a chamada ao modelo de IA real
    if force_result == "ai":
        is_ai = True
        confidence = 0.94
    elif force_result == "real":
        is_ai = False
        confidence = 0.91
    else:
        is_ai = random.choice([True, False])
        confidence = round(random.uniform(0.55, 0.99), 2)

    return AnalysisResult(
        filename=file.filename,
        is_ai_generated=is_ai, 
        confidence=confidence,
        label="AI-generated" if is_ai else "Real"
    )