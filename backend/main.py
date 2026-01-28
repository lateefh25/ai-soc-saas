from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine.ai_risk_model import model

app = FastAPI()

class AlertRequest(BaseModel):
    alert: str

@app.get("/")
def root():
    return {"status": "SOC AI Backend Running"}

@app.post("/analyze")
def analyze(request: AlertRequest):
    return model.analyze_alert(request.alert)
