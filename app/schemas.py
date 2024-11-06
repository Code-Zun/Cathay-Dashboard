from pydantic import BaseModel

class FlightDataSchema(BaseModel):
    airline: str
    capacity: int
    frequency: int

    class Config:
        orm_mode = True