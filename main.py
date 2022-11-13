import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import endpoints.authentication as auth_endpoints
import endpoints.comment as comment_endpoints
import endpoints.inbody as inbody_endpoints
import endpoints.post as post_endpoints
import endpoints.user as user_endpoints
from api.router import graphql_router
from container import Container


container = Container()
db = container.db()
db.create_database()

fast_app = FastAPI()
fast_app.container = container
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
fast_app.mount('/images',
               StaticFiles(directory=os.path.join(os.getcwd(), "images")),
               name="images")
