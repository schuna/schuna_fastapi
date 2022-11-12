from pydantic import BaseModel


class TokenPayload(BaseModel):
    status: str = 'success'
    sub: str = None
    exp: int = None


class TokenDataError(BaseModel):
    status: str
    message: str
