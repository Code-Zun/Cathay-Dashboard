from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://userAldo:Rivaldo@localhost/Cathay-Dashboard"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class FlightData(Base):
    __tablename__ = "flight_data"

    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String, index=True)
    capacity = Column(Integer)
    frequency = Column(Integer)