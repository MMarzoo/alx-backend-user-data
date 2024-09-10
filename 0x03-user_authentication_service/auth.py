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


def _generate_uuid() -> str:
    """
    Returns string repr of a new UUID
    Use uuid module
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user in the database
        Returns: User Object
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_pass = _hash_password(password)
            user = self._db.add_user(email, hashed_pass)

            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Expect email and password required arguments
        Returns a boolean
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False
