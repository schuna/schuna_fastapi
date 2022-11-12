from typing import Iterator

# noinspection PyPackageRequirements
import strawberry

from api.fields import InBodySchema
from api.resolvers import get_inbodies
from common.auth import IsAuthenticated


@strawberry.type
class Query:
    inbodies: list[InBodySchema] = strawberry.field(
        resolver=get_inbodies,
        permission_classes=[IsAuthenticated]
    )


schema = strawberry.Schema(
    query=Query,
)
