#!/usr/bin/env python3
""" API authentication class module """


import os
from flask import request
from typing import List, TypeVar


class Auth():
    """ Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns True if the path is not in the
        list of strings excluded_paths
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Request validation """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ implement later """
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
