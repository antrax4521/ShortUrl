# coding: utf-8
from datetime import datetime
from email.policy import default
from xmlrpc.client import Boolean
from sqlalchemy import Column, DateTime, ForeignKey,  String, INTEGER, Boolean
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


# Base = declarative_base()
from app.db.base_class import Base
metadata = Base.metadata

class Shortener(Base):
    """
    This model save the url to redirect
    """
    __tablename__ = 'shortener'

    id = Column(INTEGER, primary_key=True, nullable=False, unique=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.current_timestamp(), nullable=True)
    original_url = Column(String(255), nullable=False)
    short_uuid = Column(String(10), nullable=False)
    deleted = Column(Boolean, nullable=True)

    

class ShortenerLogs(Base):
    """
    This action stores the times
    """
    __tablename__ = 'shortener_logs'

    id = Column(INTEGER, primary_key=True, nullable=False, unique=True, autoincrement=True)
    shortener_id = Column(INTEGER, ForeignKey('shortener.id'), nullable=False) 
    created_at = Column(DateTime, server_default=func.current_timestamp(), nullable=True)

    relationship(Shortener)