from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status
from sqlmodel import col, select, Session

from models import Like, Post, PostPublic, UserProfile, UserPublic, User,Follow

from dependencies import CurrentUser, SessionDep, get_user_or_404


from sqlalchemy import func  # Importa `func` de sqlalchemy para contar filas

router = APIRouter(prefix="/users", tags=["users"])

def to_profile(db: Session, user: User) -> UserProfile:
    # Dos conteos en direcciones OPUESTAS sobre la misma tabla:
    followers = db.exec(
        select(func.count()).select_from(Follow).where(Follow.followed_id == user.id)
    ).one()  # filas donde user es el SEGUIDO
    following = db.exec(
        select(func.count()).select_from(Follow).where(Follow.follower_id == user.id)
    ).one()  # filas donde user es el SEGUIDOR
    return UserProfile.model_validate(
        user, update={"followers_count": followers, "following_count": following}
    )


@router.get("/{user_id}", response_model=UserProfile)
def read_user(user_id: int, db: SessionDep):
    user = get_user_or_404(db, user_id)
    return to_profile(db, user)


@router.get("/{user_id}/posts", response_model=list[PostPublic])
def read_user_posts(user_id: int, db: SessionDep):
    return get_user_or_404(db, user_id).posts


@router.get("/{user_id}/likes", response_model=list[PostPublic])
def read_user_likes(
    user_id: int, db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 20
):
    """Los posts a los que este usuario le dio like (el más reciente primero)."""
    # TODO 6 (DESAFÍO, sin pistas de código): es el espejo del TODO 5.
    #   Allá: de un post → sus usuarios.   Acá: de un usuario → sus posts.
    #   Necesitas select(Post), un join con Like, y filtrar por Like.user_id.
    #   Recuerda: 404 si el usuario no existe, y orden/paginación como en los otros listados.
    #   (Agrega a los imports de arriba lo que necesites: Like, Post.)
    #raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "TODO 6: posts que le gustaron")
    get_user_or_404(db, user_id)
    stmt = (
        select(Post)
        .join(Like, col(Like.post_id) == col(Post.id))
        .where(Like.user_id == user_id)
        .order_by(col(Like.created_at).desc())
        .offset(offset)
        .limit(limit)
    )
    return db.exec(stmt).all()

