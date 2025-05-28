#!/usr/bin/env python3
""" Session authentication module """
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Session Authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if type(user_id) is str:
            session_id = uuid4()
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None
