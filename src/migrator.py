class Migrator:
    def __init__(self, root_path='/'):
        """
        Constructor of Migrator
        :param root_path: root_path for migration
        """
        self.root_path = root_path

    def migrate(self, migration_file, sub_path='/') -> bool:
        """
        Migrate from migration_file to root_path + sub_path
        :param migration_file: Migration file. Supposed to be tar
        :param sub_path:
        :return: True if success else False
        """

    def dump(self, migration_file, sub_path='/') -> bool:
        """
        Dump root_path + sub_path to migration_file recursively
        :param migration_file: Migration file. Supposed to be tar
        :param sub_path:
        :return: True if success else False
        """
