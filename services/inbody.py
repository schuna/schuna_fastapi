from typing import Iterator

from common.response import CustomResponse
from models.inbody import InBody
from repositories.inbody import InBodyRepository
from schemas.inbody import InBodyBase


class InBodyService:
    def __init__(self, inbody_repository: InBodyRepository) -> None:
        self.inbody_repository = inbody_repository

    def create_inbody(self, item: InBodyBase) -> CustomResponse:
        return self.inbody_repository.add(item)

    def get_inbodies(self, user_id: int) -> Iterator[InBody]:
        return self.inbody_repository.get_all(user_id)
