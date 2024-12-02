from fastapi import APIRouter, Depends

from server.dependencies import (
    RequestDependenciesBase,
    get_unauthenticated_request_dependencies,
)

router = APIRouter()


@router.post("/login")
async def login(
    req_body: dict,
    req_dep: RequestDependenciesBase = Depends(
        get_unauthenticated_request_dependencies
    ),
) -> None:
    pass
