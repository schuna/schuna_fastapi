from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from schemas.comment import Comment


class User(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    user_id: int
    timestamp: Optional[datetime] = datetime.now()


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    user: User
    timestamp: datetime
    comments: List[Comment]

    class Config:
        orm_mode = True
