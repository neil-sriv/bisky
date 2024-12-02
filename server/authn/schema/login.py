from pydantic import BaseModel


class LoginPost(BaseModel):
    handle: str
