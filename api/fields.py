from datetime import datetime
import models.inbody

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
