import ldap


class AuthManager:
    def __init__(self, server="127.0.0.1"):
        """
        Constructor of AuthManager
        :param server: AuthManager's LDAP server
        """
        self.server = server

    # TODO: Check how to make LDAP client
