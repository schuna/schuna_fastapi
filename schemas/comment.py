from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    text: str
    username: str
    post_id: int
    timestamp: Optional[datetime] = datetime.now()


class CommentDisplay(BaseModel):
    id: int
    text: str
    username: str
    timestamp: datetime

    class Config:
        orm_mode = True
