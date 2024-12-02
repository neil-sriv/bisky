from fastapi import APIRouter

from server.authn.api import login

router = APIRouter()

router.include_router(login.router, prefix="/login", tags=["login"])
