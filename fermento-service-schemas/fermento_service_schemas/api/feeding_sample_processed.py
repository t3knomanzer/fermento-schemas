from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class FeedingSampleProcessedSchema(BaseModel):
    """
    Schema for processed feeding sample data.
    """

    id: int
    feeding_sample_id: int
    temperature: float
    humidity: float
    co2: float
    growth: float
    growth_rate: float
    acceleration: float
    running_max: float
    running_min: float
    stage_estimate: str
    timestamp: datetime  # ISO format string


class FeedingSampleProcessedCreateSchema(BaseModel):
    """
    Schema for processed feeding sample data.
    """

    feeding_sample_id: int
    temperature: float
    humidity: float
    co2: float
    growth: float
    growth_rate: float
    acceleration: float
    running_max: float
    running_min: float
    stage_estimate: str


class FeedingSampleProcessedUpdateSchema(BaseModel):
    """
    Schema for processed feeding sample data.
    """

    feeding_sample_id: Optional[int]
    temperature: Optional[float]
    humidity: Optional[float]
    co2: Optional[float]
    growth: Optional[float]
    growth_rate: Optional[float]
    acceleration: Optional[float]
    running_max: Optional[float]
    running_min: Optional[float]
    stage_estimate: Optional[str]
