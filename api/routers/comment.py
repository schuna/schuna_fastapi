from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status

from container import Container
from schemas.comment import CommentBase, CommentDisplay
from services.comment import CommentService

router = APIRouter(
    prefix="/comment",
    tags=["comment"]
)


@router.post('/', response_model=CommentDisplay)
@inject
def create_comment(request: CommentBase, comment_service: CommentService = Depends(Provide[Container.comment_service])):
    response = comment_service.create_comment(request)
    if response.success:
        return response.data
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{response.message}")


# noinspection PyShadowingBuiltins
@router.get("/all/{post_id}", response_model=List[CommentDisplay])
@inject
def get_comments(post_id: int, comment_service: CommentService = Depends(Provide[Container.comment_service])):
    return comment_service.get_comments(post_id)
