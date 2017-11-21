import os
import shutil
import tarfile

from unittest import TestCase

from src.migrator import Migrator


class TestMigrator(TestCase):
    temp_directory_path = "tmp"
    space_directory_name = "space"
    migration_file_name = "dump.tar.gz"
    file_name1 = "test1.txt"
    file_name2 = "test2.txt"
    sentence1 = "Mr. and Mrs. Dursley of number four, Privet Drive, were proud" + \
                " to say that they were perfectly normal, thank you very much."
    sentence2 = "I'm going to have a lot of fun with Dudley this summer..."

    def setUp(self):
        if not os.path.exists(self.temp_directory_path):
            os.makedirs(self.temp_directory_path)

    def tearDown(self):
        shutil.rmtree(self.temp_directory_path)

    def test_migrate__expect_success(self):
        space_directory_path = os.path.join(self.temp_directory_path, self.space_directory_name)
        os.makedirs(space_directory_path)
        with open(os.path.join(space_directory_path, self.file_name1), 'w') as infile:
            infile.write(self.sentence1)
        with open(os.path.join(space_directory_path, self.file_name2), 'w') as infile:
            infile.write(self.sentence2)

        with tarfile.open(os.path.join(self.temp_directory_path, self.migration_file_name), 'w:gz') as infile:
            infile.add(space_directory_path, recursive=True)

        shutil.rmtree(space_directory_path)

        self.assertEqual(False, os.path.exists(space_directory_path))

        migrator = Migrator(self.temp_directory_path)
        migrator.migrate(self.migration_file_name, self.space_directory_name)

        self.assertEqual(True, os.path.exists(space_directory_path))

    def test_migrate__with_txt_file__expect_failure(self):
        with open(os.path.join(self.temp_directory_path, self.file_name1), 'w') as infile:
            infile.write(self.sentence1)

        migrator = Migrator(self.temp_directory_path)
        result = migrator.migrate(self.migration_file_name, self.temp_directory_path)

        self.assertEqual(False, result)

    def test_dump__expect_success(self):
        space_directory_path = os.path.join(self.temp_directory_path, self.space_directory_name)
        os.makedirs(space_directory_path)
        with open(os.path.join(space_directory_path, self.file_name1), 'w') as infile:
            infile.write(self.sentence1)
        with open(os.path.join(space_directory_path, self.file_name2), 'w') as infile:
            infile.write(self.sentence2)

        migrator = Migrator(space_directory_path)
        migrator.dump(self.migration_file_name)
