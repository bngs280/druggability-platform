from fastapi import FastAPI
from pydantic import BaseModel

from src.inference.predict_pipeline import predict_from_uniprot

app = FastAPI(title="Druggability AI API")


# -----------------------
# Request schema
# -----------------------
class PredictRequest(BaseModel):
    uniprot: str


# -----------------------
# Health check endpoint (VERY IMPORTANT)
# -----------------------
@app.get("/")
def home():
    return {"status": "API running"}


# -----------------------
# Prediction endpoint
# -----------------------
@app.post("/predict")
def predict(req: PredictRequest):

    result = predict_from_uniprot(req.uniprot)

    return {
        "uniprot": req.uniprot,
        "score": float(result["score"]),
        "prediction_class": int(result["prediction_class"]),
        "probability": result["probability"]
    }
