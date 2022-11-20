from datetime import timedelta

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from common.hash import Hash
from common.oauth2 import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from container import Container
from schemas.tokens import Token
from services.user import UserService

router = APIRouter(
    tags=["authentication"]
)


@router.post('/token', response_model=Token)
@inject
def get_token(
        response: Response,
        request: Request,
        request_form: OAuth2PasswordRequestForm = Depends(),
        user_service: UserService = Depends(Provide[Container.user_service])):
    user_response = user_service.get_user_by_name(request_form.username)
    if not user_response.success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    user = user_response.data
    if not Hash.verify(user.password, request_form.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(data={'username': user.username}, expires_delta=access_token_expires)

    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    request.session['username'] = user.username
    print(request.cookies.get('session'))

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username
    }
