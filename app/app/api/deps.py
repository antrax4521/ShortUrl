from typing import Generator
from xmlrpc.client import Boolean

from fastapi import Depends, Request, status
# from jose import jwt
# from pydantic import ValidationError
from sqlalchemy.orm import Session

# from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()

        yield db
    finally:

        db.close()
