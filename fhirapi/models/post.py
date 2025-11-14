from pydantic import BaseModel


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int

    class Config:
        orm_mode = True  # return_value.body instead of return_value["body"]


class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int

    class Config:
        orm_mode = True  # return_value.body instead of return_value["body"]


class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]
