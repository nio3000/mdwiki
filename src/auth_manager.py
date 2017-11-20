import ldap

from enum import Enum


class ServerResult(Enum):
    SUCCESS = 200
    SERVER_NOT_FOUND = 404


class LoginResult(ServerResult):
    WRONG_ID_OR_PASSWORD = 403


class RequestAccessResult(ServerResult):
    DENIED = 403


class AuthManager:
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
