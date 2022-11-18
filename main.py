import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import api.routers.upload_image as upload_image_endpoints
import api.routers.authentication as auth_endpoints
import api.routers.comment as comment_endpoints
import api.routers.inbody as inbody_endpoints
import api.routers.post as post_endpoints
import api.routers.user as user_endpoints
from api.routers.graphql import graphql_router
from container import Container
from webapps.base import api_router as web_app_router

container = Container()
db = container.db()
db.create_database()

fast_app = FastAPI()
fast_app.container = container
fast_app.include_router(web_app_router)
fast_app.include_router(upload_image_endpoints.router)
fast_app.include_router(inbody_endpoints.router)
fast_app.include_router(comment_endpoints.router)
fast_app.include_router(auth_endpoints.router)
fast_app.include_router(user_endpoints.router)
fast_app.include_router(post_endpoints.router)
fast_app.include_router(graphql_router, prefix='/graphql')

origins = [
    'http://localhost:3000',
    'http://localhost:3001'
]

fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)
fast_app.mount('/static', StaticFiles(directory=os.path.join(os.getcwd(), "static")), name="static")
