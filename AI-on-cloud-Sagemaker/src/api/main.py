from sqlalchemy.orm import Session

from src.database.database import SessionLocal
from src.database.crud import save_prediction
from src.database.database import engine
from src.database.database import Base

import src.database.models
from fastapi import FastAPI,Depends

from src.api.schemas import (
    CustomerData,
    PredictionResponse
)

from src.api.predictor import predict


app = FastAPI(

    title="AI on Cloud using AWS SageMaker",

    version="1.0"

)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():

    return {

        "message": "Customer Churn Prediction API"

    }


@app.get("/health")
def health():

    return {

        "status": "Healthy"

    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def prediction(
    customer: CustomerData,
    db: Session = Depends(get_db)
):

    result = predict(customer.model_dump())

    save_prediction(
        db=db,
        prediction=result["prediction"],
        probability=result["probability"],
        risk_level=result["risk_level"]
    )

    return result

from src.database.crud import get_all_predictions

@app.get("/history")
def prediction_history(
    db: Session = Depends(get_db)
):

    predictions = get_all_predictions(db)

    return [

        {
            "id": p.id,
            "prediction": p.prediction,
            "probability": p.probability,
            "risk_level": p.risk_level,
            "created_at": p.created_at
        }

        for p in predictions

    ]