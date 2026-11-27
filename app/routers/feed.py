"""El feed: los posts de las personas a las que sigo."""
from typing import Annotated

from fastapi import APIRouter, Query
from sqlmodel import col, select

from dependencies import CurrentUser, SessionDep
from models import Follow, Post, PostWithLikes
from routers.posts import posts_with_likes, to_post_with_likes

router = APIRouter(prefix="/feed", tags=["feed"])


@router.get("", response_model=list[PostWithLikes])
def read_feed(
    db: SessionDep,
    current_user: CurrentUser,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 20,
):
    followed_ids = select(Follow.followed_id).where(
        Follow.follower_id == current_user.id
    )

    stmt = (
        posts_with_likes()
        .where(col(Post.author_id).in_(followed_ids))
        .order_by(col(Post.created_at).desc())
        .offset(offset)
        .limit(limit)
    )

    return [to_post_with_likes(row) for row in db.exec(stmt).all()]