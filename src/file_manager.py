import os


class FileManager:
    def __init__(self, file_path: str = '/'):
        """
        Constructor of FileManager
        :param file_path: FileManager's default file_path. FileManager use `self.file_path` as prefix if exist.
        :type file_path: str
        """
        self.file_path = file_path

    def __relative_path(self, file_path):
        if file_path is None:
            return self.file_path
        else:
            return os.path.join(self.file_path, file_path)

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
            with open(relative_path, 'w') as infile:
                infile.write(content)
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
            with open(relative_path, 'r') as outfile:
                return os.linesep.join(outfile.readlines())

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
            with open(relative_path, 'w') as infile:
                infile.write(content)
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
