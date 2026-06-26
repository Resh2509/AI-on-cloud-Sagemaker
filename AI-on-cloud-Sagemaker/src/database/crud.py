from sqlalchemy.orm import Session

from src.database.models import Prediction


def save_prediction(
    db: Session,
    prediction: str,
    probability: float,
    risk_level: str
):

    new_prediction = Prediction(

        prediction=prediction,

        probability=probability,

        risk_level=risk_level

    )

    db.add(new_prediction)

    db.commit()

    db.refresh(new_prediction)

    return new_prediction


def get_all_predictions(
    db: Session
):

    return db.query(Prediction).all()