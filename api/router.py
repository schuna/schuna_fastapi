from dependency_injector.wiring import Provide, inject
from fastapi import Depends
# noinspection PyPackageRequirements
from strawberry.asgi import GraphQL
# noinspection PyPackageRequirements
from strawberry.fastapi import GraphQLRouter, BaseContext

from api.schema import schema
from container import Container
from services.comment import CommentService
from services.inbody import InBodyService
from services.post import PostService
from services.user import UserService


class CustomContext(BaseContext):
    @inject
    def __init__(
            self,
            user_service: UserService = Depends(Provide[Container.user_service]),
            post_service: PostService = Depends(Provide[Container.post_service]),
            comment_service: CommentService = Depends(Provide[Container.comment_service]),
            inbody_service: InBodyService = Depends(Provide[Container.inbody_service])
    ):
        super().__init__()
        self.inbody_service = inbody_service
        self.comment_service = comment_service
        self.post_service = post_service
        self.user_service = user_service


def custom_context_dependency() -> CustomContext:
    return CustomContext()


async def get_context(custom_context=Depends(custom_context_dependency), ):
    return custom_context


graphql_router = GraphQLRouter(schema, context_getter=get_context, )
graphql_app = GraphQL(schema)
