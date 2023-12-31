from flask_login import UserMixin
from sqlalchemy import DATETIME, Column, Integer, String
from sqlalchemy.sql import func

from factory.extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(60), unique=True, nullable=False)
    email = Column(String(60), nullable=False)
    avatar = Column(String(60), nullable=False, server_default="default-bear.svg")
    location = Column(String(60), nullable=True, default=None)
    blurb = Column(String(280), nullable=True, default=None)
    password = Column(String(60), nullable=False)
    created_at = Column(DATETIME, server_default=func.now())
    updated_at = Column(DATETIME, onupdate=func.now())
