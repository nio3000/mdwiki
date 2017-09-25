import unittest
import os
import shutil
from src.file_manager import FileManager


class FileManagerTest(unittest.TestCase):
    temp_directory_path = "tmp"
    sentence1 = "Mr. and Mrs. Dursley of number four, Privet Drive, were proud" + \
                " to say that they were perfectly normal, thank you very much."
    sentence2 = "I'm going to have a lot of fun with Dudley this summer..."

    def setUp(self):
        if not os.path.exists(self.temp_directory_path):
            os.makedirs(self.temp_directory_path)

    def tearDown(self):
        shutil.rmtree(self.temp_directory_path)

    def test_create_expect_success(self):
        file_name = "test_create.txt"

        fm = FileManager(self.temp_directory_path)
        self.assertEqual(True, fm.create(self.sentence1, file_name))

        with open(os.path.join(self.temp_directory_path, file_name), 'r') as outfile:
            self.assertEqual(self.sentence1, outfile.readline())

    def test_update_expect_success(self):
        file_name = "test_update.txt"

        with open(os.path.join(self.temp_directory_path, file_name), 'w') as infile:
            infile.write(self.sentence1)

        fm = FileManager(self.temp_directory_path)
        self.assertEqual(True, fm.update(self.sentence2, file_name))

        with open(os.path.join(self.temp_directory_path, file_name), 'r') as outfile:
            self.assertEqual(self.sentence2, outfile.readline())

    def test_read_expect_success(self):
        file_name = "test_read.txt"

        with open(os.path.join(self.temp_directory_path, file_name), 'w') as infile:
            infile.write(self.sentence1)

        fm = FileManager(self.temp_directory_path)
        self.assertEqual(self.sentence1, fm.read(file_name))

    def test_delete_expect_success(self):
        file_name = "test_delete.txt"

        with open(os.path.join(self.temp_directory_path, file_name), 'w') as infile:
            infile.write(self.sentence1)

        fm = FileManager(self.temp_directory_path)
        self.assertEqual(True, fm.delete(file_name))

        self.assertEqual(False, os.path.exists(os.path.join(self.temp_directory_path, file_name)))


if __name__ == '__main__':
    unittest.main()
