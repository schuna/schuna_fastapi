from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates

from container import Container
from services.post import PostService

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
@inject
async def home(
        request: Request,
        post_service: PostService = Depends(Provide[Container.post_service]),
        msg: str = None):
    posts = post_service.get_posts()
    return templates.TemplateResponse(
        "pages/home.html", {"request": request, "posts": posts, "msg": msg}
    )
