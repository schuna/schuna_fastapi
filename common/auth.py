from typing import Any, Union, Awaitable, Optional

# noinspection PyPackageRequirements
from jose import jwt, JWTError
from pydantic import ValidationError
# noinspection PyPackageRequirements
from starlette.requests import Request
# noinspection PyPackageRequirements
from starlette.websockets import WebSocket
# noinspection PyPackageRequirements
from strawberry.permission import BasePermission
# noinspection PyPackageRequirements
from strawberry.types import Info

from common.oauth2 import SECRET_KEY, ALGORITHM
from schemas.auth import TokenPayload, TokenDataError
from datetime import datetime


def decode_jwt(token: str, secret_key: str) -> Optional[TokenPayload]:
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            return None

        return token_data
    except(JWTError, ValidationError):
        return None


def decode_access_token(token) -> Optional[TokenPayload]:
    return decode_jwt(token, SECRET_KEY)


class VerifyToken:
    def __init__(self, token):
        self.token = token

    def verify(self) -> Union[TokenPayload, TokenDataError]:
        token_data = decode_access_token(self.token)
        if token_data is None:
            return TokenDataError(status="error", message="Invalid token or expired token")

        return token_data


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    async def has_permission(self, source: Any, info: Info, **kwargs) -> Union[bool, Awaitable[bool]]:
        request: Union[Request, WebSocket] = info.context.request
        if "authorization" in request.headers:
            result = VerifyToken(request.headers['authorization'][7:]).verify()
            if result.status != "error":
                return True

        return False
