import logging
from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from common.response import CustomResponse
from models.comment import Comment
from schemas.comment import CommentBase


# noinspection PyShadowingBuiltins
class CommentRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    # Create
    def add(self, item: CommentBase) -> CustomResponse:
        with self.session_factory() as session:
            try:
                comment = Comment(**item.dict())
                session.add(comment)
                session.commit()
                session.refresh(comment)
                return CustomResponse(comment)
            except IntegrityError:
                logging.info("Duplicated Error")
                session.rollback()
                return CustomResponse({}, False, f"Duplicated Error {item.json()}")

    # Read
    def get_all(self, post_id: int) -> Iterator[Comment]:
        with self.session_factory() as session:
            return session.query(Comment).filter(Comment.post_id == post_id).all()

