import os
import shutil
import string
import random

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File

from common.utils import create_dir

router = APIRouter(
    tags=["upload_image"]
)


@router.post("/upload_image")
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_string = ''.join(random.choice(letter) for _ in range(6))
    new = f"_{rand_string}."
    filename = new.join(image.filename.rsplit('.', 1))
    static_path = os.path.join(os.getcwd(), "static")
    root_path = os.path.join(static_path, "images")

    path = os.path.join(root_path, filename)

    create_dir(root_path)
    try:
        with open(path, 'w+b') as wf:
            shutil.copyfileobj(image.file, wf)
        return {'filename': path}
    except OSError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Error: {e}')
