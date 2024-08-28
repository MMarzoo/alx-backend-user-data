#!/usr/bin/env python3
"""
Encrypting passwords
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns a salted, hashed password, which is a byte string
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if the hashed password matches the password
    """
    vailed = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        vailed = True
    return vailed
