import logging
from sqlalchemy.orm import Session
from pydantic import HttpUrl

from app.models.shortener import Shortener, ShortenerLogs
from app.api.api_v1.shorturl.utils import short_uuid_generator
from sqlalchemy.exc import DataError

def save_original_url(
    db: Session, 
    original_url: HttpUrl
) -> Shortener:
    """
    Create a record to UserPrivateProfile
    """
    try:
        sh_obj = Shortener()
        sh_obj.original_url = original_url
        sh_obj.short_uuid = short_uuid_generator()
        
        db.add(sh_obj)
        db.commit()

        return sh_obj
    except DataError as e:
        logging.exception(f"Server Error {str(e)}", exc_info=True)


def save_shortener_log(
    db: Session, 
    shortener_id: str
) -> ShortenerLogs:
    """
    Create a record to UserPrivateProfile
    """
    try:
        shl_obj = ShortenerLogs()
        shl_obj.shortener_id = shortener_id
        
        db.add(shl_obj)
        db.commit()

        return shl_obj
    except DataError as e:
        logging.exception(f"Server Error {str(e)}", exc_info=True)


def get_original_url(
    db: Session, 
    short_key: str
) -> Shortener:
    """
    Busca al cliente al que pertenece 
    """
    try:

        return db.query(Shortener) \
        .filter(Shortener.short_uuid == short_key) \
        .one_or_none()
    except DataError as e:
        logging.exception(f"Server Error {str(e)}", exc_info=True)

