from sqlalchemy.orm import Session
from app.api.api_v1.shorturl.crud import save_shortener_log
from sqlalchemy.orm.query import Query



def perform_shortener_log(db: Session, shortener_id: str) -> Query:
    """
    Excecute a background task to perform a new row into table
    ShortenerLog
    """
    return save_shortener_log(db, shortener_id)