#!/usr/bin/env python3
""" Module Basic_auth for user authentication
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class BasicAuth for user authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method to extract base64 encoded string from authorization header
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]
        return encoded
