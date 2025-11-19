from pydantic import BaseModel, ConfigDict


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True  # return_value.body instead of return_value["body"]
    )


class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True  # return_value.body instead of return_value["body"]
    )


class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]


class PostLikeIn(BaseModel):
    post_id: int


class PostLike(PostLikeIn):
    id: int
    user_id: int
