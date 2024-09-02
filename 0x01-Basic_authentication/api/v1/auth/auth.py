#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication 
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'

        astericks = [stars[:-1]
                     for stars in excluded_paths if stars[-1] == '*']

        for stars in astericks:
            if path.startswith(stars):
                return False

        if path in excluded_paths:
            return False
        return True

def authorization_header(self, request=None) -> str:
    """ Method to get the Authorization header
    """
    if request is None:
        return None
    return request.headers.get("Authorization", None)

def current_user(self, request=None) -> TypeVar('User'):
    """ Method to get the current user
    """
    return None
