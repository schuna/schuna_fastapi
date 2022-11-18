from datetime import datetime
from typing import List
from typing import Optional

from fastapi import Request


class PostCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.image_url: Optional[str] = None
        self.image_url_type: Optional[str] = None
        self.caption: Optional[str] = None
        self.user_id: Optional[str] = None
        self.timestamp: Optional[datetime] = datetime.now()

    async def load_data(self):
        form = await self.request.form()
        self.image_url = form.get("image_url")
        self.image_url_type = form.get("image_url_type")
        self.caption = form.get("caption")
        self.user_id = form.get("user_id")
        self.timestamp = form.get("timestamp")

    def is_valid(self):
        if not self.image_url or not len(self.image_url) >= 4:
            self.errors.append("A valid title is required")
        if not self.image_url_type:
            self.errors.append("Valid type is absolute or relative")
        if not self.caption or not len(self.caption) >= 1:
            self.errors.append("A valid caption is required")
        if not self.user_id:
            self.errors.append("User ID is required")
        if not self.errors:
            return True
        return False
