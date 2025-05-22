from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class DeliveryRequest(BaseModel):
    store_segment: int
    order_delivery_fee: float
    value_to_fee_ratio: float
    order_amount: float
    is_weekend: int
    channel_type: int

# Carregar o modelo salvo
model = joblib.load('delivery_model.joblib')

@app.post("/predict")
def predict(data: DeliveryRequest):
    # Preparar dados para o modelo
    df = pd.DataFrame([data.dict()])
    pred_distance = model.predict(df)[0]
    
    velocity_kmh = 20
    time_min = (pred_distance / (velocity_kmh * 1000 / 3600)) / 60
    
    intervalo = "±15 min" if pred_distance <= 1000 else "±10 min" if pred_distance <= 3000 else "±20 min"
    
    return {
        "distancia_m": round(pred_distance, 2),
        "tempo_min": round(time_min, 2),
        "intervalo": intervalo
    }
