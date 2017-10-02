import unittest
import os
import shutil
from src.file_manager import FileManager


class FileManagerTest(unittest.TestCase):
    temp_directory_path = "tmp"
    file_name = "test.txt"
    sentence1 = "Mr. and Mrs. Dursley of number four, Privet Drive, were proud" + \
                " to say that they were perfectly normal, thank you very much."
    sentence2 = "I'm going to have a lot of fun with Dudley this summer..."

    def setUp(self):
        if not os.path.exists(self.temp_directory_path):
            os.makedirs(self.temp_directory_path)

    def tearDown(self):
        shutil.rmtree(self.temp_directory_path)

    def test_create__expect_success(self):
        fm = FileManager(self.temp_directory_path)
        self.assertEqual(True, fm.create(self.sentence1, self.file_name))

        with open(os.path.join(self.temp_directory_path, self.file_name), 'r') as infile:
            self.assertEqual(self.sentence1, infile.readline())

    def test_update__expect_success(self):
        with open(os.path.join(self.temp_directory_path, self.file_name), 'w') as outfile:
            outfile.write(self.sentence1)

        fm = FileManager(self.temp_directory_path)
        self.assertEqual(True, fm.update(self.sentence2, self.file_name))

        with open(os.path.join(self.temp_directory_path, self.file_name), 'r') as infile:
            self.assertEqual(self.sentence2, infile.readline())

    def test_read__expect_success(self):
        with open(os.path.join(self.temp_directory_path, self.file_name), 'w') as outfile:
            outfile.write(self.sentence1)

        fm = FileManager(self.temp_directory_path)
        self.assertEqual(self.sentence1, fm.read(self.file_name))

    def test_delete__expect_success(self):
        with open(os.path.join(self.temp_directory_path, self.file_name), 'w') as outfile:
            outfile.write(self.sentence1)

        fm = FileManager(self.temp_directory_path)
        self.assertEqual(True, fm.delete(self.file_name))

        self.assertEqual(False, os.path.exists(os.path.join(self.temp_directory_path, self.file_name)))


if __name__ == '__main__':
    unittest.main()
