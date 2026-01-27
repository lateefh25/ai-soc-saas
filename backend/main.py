from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Alert(BaseModel):
    text: str

@app.post("/analyze")
def analyze_alert(alert: Alert):
    return {
        "decision": "False Positive",
        "confidence": "78%"
    }
