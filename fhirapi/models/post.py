from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int
    user_id: int
    image_url: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True  # return_value.body instead of return_value["body"]
    )


class UserPostWithLikes(UserPost):
    likes: int

    model_config = ConfigDict(
        from_attributes=True  # return_value.likes instead of return_value["likes"]
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
    post: UserPostWithLikes
    comments: list[Comment]


class PostLikeIn(BaseModel):
    post_id: int


class PostLike(PostLikeIn):
    id: int
    user_id: int
