#!/usr/bin/env python3
""" Session authentication module """
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Session Authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create a Session ID for a user_id"""
        if type(user_id) is str:
            session_id = uuid4()
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
        return None
