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
    password = Column(String(60), nullable=False)
    created_at = Column(DATETIME, server_default=func.now())
    updated_at = Column(DATETIME, server_onupdate=func.now())
