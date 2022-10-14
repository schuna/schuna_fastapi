from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class InBodyBase(BaseModel):
    weight: float
    fat_rate: float
    timestamp: Optional[datetime] = datetime.now()
    user_id: float


class InBodyDisplay(BaseModel):
    weight: float
    fat_rate: float
    timestamp: datetime

    class Config:
        orm_mode = True
