from sqlalchemy.orm import Session
from . import models, schemas

def get_flight_data(db: Session, flight_id: int):
    return db.query(models.FlightData).filter(models.FlightData.id == flight_id).first()

def create_flight_data(db: Session, flight_data: schemas.FlightDataSchema):
    db_flight_data = models.FlightData(**flight_data.dict())
    db.add(db_flight_data)
    db.commit()
    db.refresh(db_flight_data)
    return db_flight_data