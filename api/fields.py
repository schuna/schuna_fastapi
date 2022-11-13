from datetime import datetime
from typing import Optional

# noinspection PyPackageRequirements
import strawberry


@strawberry.type
class UserSchema:
    id: strawberry.ID
    username: str


@strawberry.type
class InBodySchema:
    id: strawberry.ID
    weight: float
    fat_rate: float
    timestamp: datetime
    user: UserSchema


@strawberry.input
class InBodyCreate:
    weight: float
    fat_rate: float
    timestamp: Optional[datetime] = datetime.now()
    user_id: strawberry.ID
