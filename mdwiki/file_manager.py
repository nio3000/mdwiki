from os import access, W_OK
from os.path import join

class FileManager:
    def __init__(self, file_path = None):
        """
        Constructor of FileManager
        :param file_path: FileManager's default file_path. FileManager use `self.file_path` as prefix if exist.
        :type file_path: str
        """
        self.file_path = file_path

    def __validate(self, file_path):
        """
        Check file_path is valid or not. Doesn't use `self.file_path` as prefix.
        :param file_path: Where file to validate is.
        :type file_path: str
        :return:
        """

    def __relative_path(self, file_path):
        """
        Return relative path of the instance with `file_path`
        :param file_path:
        :return:
        """

    def create(self, content, file_path = None):
        """
        Create file. Use `self.file_path` as prefix.
        :param content: Content of file. Can't be None.
        :type content: str
        :param file_path: Where this method create file.
        :type file_path: str
        :return: If success return `True`, else `False`
        """

    def read(self, file_path = None):
        """
        Read file. Use `self.file_path` as prefix.
        :param file_path: Where file to read is.
        :return: If success return `True`, else `False`
        """

    def update(self, content, file_path = None):
        """
        Update file. Use `self.file_path` as prefix.
        :param content:  Content of file. Can't be None.
        :type content: str
        :param file_path:  Where file to update is.
        :return: If success return `True`, else `False`
        """

    def delete(self, file_path = None):
        """
        Delete file. Use self.file_path as prefix.
        :param file_path: Where file to delete is.
        :return: If success return `True`, else `False`
        """

