from fastapi import HTTPException, status
# noinspection PyPackageRequirements
from strawberry.types import Info

from api.fields import InBodySchema, InBodyCreate
from schemas.inbody import InBodyBase


async def get_inbodies(user_id: int, info: Info) -> list[InBodySchema]:
    return info.context.inbody_service.get_inbodies(user_id)


async def create_inbody(data: InBodyCreate, info: Info) -> InBodySchema:
    entry = InBodyBase(
        **data.__dict__
    )
    response = info.context.inbody_service.create_inbody(entry)
    if response.success:
        return response.data
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{response.message}")
