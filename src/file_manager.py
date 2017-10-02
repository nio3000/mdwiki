import os


class FileManager:
    def __init__(self, directory_path: str = '/'):
        """
        Constructor of FileManager
        :param directory_path: FileManager's default file_path. FileManager use `self.file_path` as prefix if exist.
        """
        self.directory_path = directory_path

    def create(self, content: str, file_path: str = None) -> bool:
        """
        Create file. Use `self.file_path` as prefix.
        :param content: Content of file. Can't be None.
        :param file_path: Where this method create file.
        :return: If success return `True`, else `False`
        """
        relative_path = self.__relative_path(file_path)
        if os.path.exists(relative_path):
            return False
        else:
            with open(relative_path, 'w') as outfile:
                outfile.write(content)
            return True

    def read(self, file_path: str = None) -> str:
        """
        Read file. Use `self.file_path` as prefix.
        :param file_path: Where file to read is.
        :return: If success return `True`, else `False`
        """
        relative_path = self.__relative_path(file_path)
        if not os.path.exists(relative_path):
            raise FileNotFoundError
        else:
            with open(relative_path, 'r') as infile:
                return os.linesep.join(infile.readlines())

    def update(self, content: str, file_path: str = None) -> bool:
        """
        Update file. Use `self.file_path` as prefix.
        :param content:  Content of file. Can't be None.
        :param file_path:  Where file to update is.
        :return: If success return `True`, else `False`
        """
        relative_path = self.__relative_path(file_path)
        if not os.path.exists(relative_path):
            return False
        else:
            with open(relative_path, 'w') as outfile:
                outfile.write(content)
            return True

    def delete(self, file_path: str = None) -> bool:
        """
        Delete file. Use self.file_path as prefix.
        :param file_path: Where file to delete is.
        :return: If success return `True`, else `False`
        """
        relative_path = self.__relative_path(file_path)
        if not os.path.exists(relative_path):
            return False
        else:
            os.remove(relative_path)
            return True

    def __relative_path(self, file_path):
        if file_path is None:
            return self.directory_path
        else:
            return os.path.join(self.directory_path, file_path)
