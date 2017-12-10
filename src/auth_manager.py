import ldap

from enum import Enum


class AuthManager:
    class _ServerResult(Enum):
        SERVER_NOT_FOUND = 0
        WRONG_REQUEST = 1

    class LoginResult(_ServerResult):
        WRONG_ID_OR_PASSWORD = 0

    class LogoutResult(_ServerResult):
        SUCCESS = 0

    class RequestAccessResult(_ServerResult):
        APPROVED = 0
        DENIED = 1

    def __init__(self, server="127.0.0.1"):
        """
        Constructor of AuthManager
        :param server: AuthManager's LDAP server
        """
        self.server = server

    def login(self, id, password):
        """
        Login to LDAP server
        :param id:
        :param password:
        :return: LoginResult
        """

    def logout(self):
        """
        Logout from LDAP server
        :return: ServerResult
        """

    def request_access(self, file_id):
        """
        Request access to the file whose id is file_id
        :param file_id:
        :return: RequestAccessResult
        """
