class GitManager:
    def __init__(self, root_path: str = '/', directory_path: str = '/'):
        """
        Constructor of GitManager
        :param root_path:
        :param directory_path:
        """

    def commit(self, file_path: str = '/') -> bool:
        """
        Commit file.
        :param file_path:
        :return: False if commit nothing
        """

    def revert(self, file_path: str = '/', revision: int = None) -> bool:
        """
        Revert file to revision.
        This only revert content. Revision will be incremented.
        :param file_path:
        :param revision:
        :return: False if revision is None or non-existence
        """

    def get_logs(self, file_path: str = '/') -> str:
        """
        Return all logs where file_path
        :param file_path:
        :return:
        """

    def get_log(self, file_path: str = '/', revision: int = None) -> str:
        """
        Return detail revision log where file_path.
        Return latest if revision is None
        :param file_path:
        :param revision:
        :return: None if revision doesn't exist
        """
