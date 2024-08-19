from sqlalchemy import create_engine, Column, String, Float, DateTime, func, Index, select
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.sqlite import DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

import uuid
import datetime

class Weather:
    tablename = "weather"

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # city = Column(String, nullable=False)
    # min_temp = Column(Float, nullable=False)
    # max_temp = Column(Float, nullable=False)
    # average_mean_temp = Column(Float, nullable=False)
    # average_mode_temp = Column(Float, nullable=False)
    # average_mean_humidity = Column(Float, nullable=False)
    # average_mode_humidity = Column(Float, nullable=False)
    # date = Column(DATETIME, nullable=False)
    # created_at = Column(DATETIME, server_default=func.now(), nullable=False)    
    # updated_at = Column(DATETIME, server_default=func.now(), nullable=False, onupdate=func.now())
    # deleted_at = Column(DATETIME, nullable=True)

class HistoricalFetches:
    tablename = "historical_fetches"

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # city = Column(String, nullable=False)
    # date = Column(DATETIME, nullable=False)
    # hash = Column(String, nullable=False, unique=True)
    # created_at = Column(DATETIME, server_default=func.now(), nullable=False)
    # updated_at = Column(DATETIME, server_default=func.now(), nullable=False, onupdate=func.now())
    # deleted_at = Column(DATETIME, nullable=True)


class DatabaseClient:
    def __init__(self) -> None:
        pass

    def add_weather_data(self, weather_data: dict):
        pass

    def get_weather_data(self, city: str, date: datetime.date):
        pass

    def add_historical_fetch(self, city: str, date: datetime.date):
        pass

    def generate_hash(self, city: str, date: datetime.date) -> str:
        pass

