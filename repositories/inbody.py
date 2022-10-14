import logging
from contextlib import AbstractContextManager
from typing import Callable, Iterator

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from common.response import CustomResponse
from models.inbody import InBody
from models.user import User
from schemas.inbody import InBodyBase


class InBodyRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    # Create
    def add(self, item: InBodyBase) -> CustomResponse:
        with self.session_factory() as session:
            try:
                inbody = InBody(**item.dict())
                session.add(inbody)
                session.commit()
                session.refresh(inbody)
                return CustomResponse(inbody)
            except IntegrityError:
                logging.info("Duplicated Error")
                session.rollback()
                return CustomResponse({}, False, f"Duplicated Error {item.json()}")

    def get_all(self, user_id: int) -> Iterator[InBody]:
        with self.session_factory() as session:
            return session.query(InBody).filter(InBody.user_id == user_id).all()
