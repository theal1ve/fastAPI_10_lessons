from fastapi import APIRouter
from .schemas import CreateUser
from . import crud

router_users = APIRouter(prefix="/users", tags=["Users"])


@router_users.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
