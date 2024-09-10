#!/usr/bin/env python3
"""
Auth Class for user attributes validation
"""

from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    Returns a salted hash of the input password
    """
    return hashpw(password.encode('utf-8'), gensalt())
