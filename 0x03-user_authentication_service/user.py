#!/usr/bin/env python3
"""
Create a SQLAlchemy model named `User`
for database table named `users`
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class User(Base):
    """
    User Class
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
