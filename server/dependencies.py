from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from fastapi import Depends

from server.sqlalchemy_base import get_db

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


@dataclass
class RequestDependenciesBase:
    db: Session


# @dataclass
# class AuthenticatedRequestDependencies(RequestDependenciesBase):
#     current_user: User


# async def get_request_dependencies(
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user),
# ) -> AuthenticatedRequestDependencies:
#     return AuthenticatedRequestDependencies(db=db, current_user=current_user)


async def get_unauthenticated_request_dependencies(
    db: Session = Depends(get_db),
) -> RequestDependenciesBase:
    return RequestDependenciesBase(db=db)
