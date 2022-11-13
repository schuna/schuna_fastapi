# noinspection PyPackageRequirements
import strawberry

from api.fields import InBodySchema
from api.resolvers import get_inbodies, create_inbody
from common.auth import IsAuthenticated


@strawberry.type
class Query:
    inbodies: list[InBodySchema] = strawberry.field(
        resolver=get_inbodies,
        permission_classes=[IsAuthenticated]
    )


@strawberry.type
class Mutation:
    create_inbody: InBodySchema = strawberry.mutation(
        resolver=create_inbody,
        permission_classes=[IsAuthenticated]
    )


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
