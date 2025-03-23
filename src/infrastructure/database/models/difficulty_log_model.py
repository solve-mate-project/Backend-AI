from sqlalchemy import Column, Integer, String, DateTime, Text
from src.infrastructure.database.database_connection import DBBase


class DifficultyLogModel(DBBase):
    __tablename__ = "difficulty_prediction_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    platform = Column(String(50), nullable=False)
    title = Column(Text, nullable=False)
    difficulty = Column(String(50), nullable=False)
    difficulty_explanation = Column(Text)
    prediction_date = Column(DateTime, nullable=False)
    model_version = Column(String(50))
