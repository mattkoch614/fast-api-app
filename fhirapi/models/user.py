from pydantic import BaseModel


class User(BaseModel):
    id: int | None = None
    email: str


# We don't want to return the password to the client
class UserIn(User):
    password: str
