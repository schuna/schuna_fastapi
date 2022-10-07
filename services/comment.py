from typing import Iterator

from common.response import CustomResponse
from models.comment import Comment
from repositories.comment import CommentRepository
from schemas.comment import CommentBase


# noinspection PyShadowingBuiltins
class CommentService:
    def __init__(self, comment_repository: CommentRepository) -> None:
        self.comment_repository = comment_repository

    def create_comment(self, item: CommentBase) -> CustomResponse:
        return self.comment_repository.add(item)

    def get_comments(self, post_id: int) -> Iterator[Comment]:
        return self.comment_repository.get_all(post_id)
