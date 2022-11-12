# noinspection PyPackageRequirements
from strawberry.types import Info

from api.fields import InBodySchema


def get_inbodies(user_id: int, info: Info) -> list[InBodySchema]:
    return info.context.inbody_service.get_inbodies(user_id)
