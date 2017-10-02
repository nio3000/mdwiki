import unittest
import os
import shutil
from src.git_manager import GitManager


class TestGitManager(unittest.TestCase):
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

    def commit_two_revision(self):
        gm = GitManager(self.temp_directory_path)
        with open(os.path.join(self.temp_directory_path, self.file_name), 'w') as outfile:
            outfile.write(self.sentence1)
        gm.commit(self.file_name)
        with open(os.path.join(self.temp_directory_path, self.file_name), 'w') as outfile:
            outfile.write(self.sentence2)
        gm.commit(self.file_name)

    def test_commit__expect_success(self):
        with open(os.path.join(self.temp_directory_path, self.file_name), 'w') as outfile:
            outfile.write(self.sentence1)
        gm = GitManager(self.temp_directory_path)
        self.assertEqual(True, gm.commit(self.file_name))
        self.assertEqual(False, gm.commit(self.file_name))

    def test_revert__expect_success(self):
        self.commit_two_revision()

        gm = GitManager(self.temp_directory_path)
        self.assertEqual(False, gm.revert(self.file_name, 3))
        with open(os.path.join(self.temp_directory_path, self.file_name), 'r') as infile:
            self.assertEqual(self.sentence2, infile.readline())
        self.assertEqual(True, gm.revert(self.file_name, 1))
        with open(os.path.join(self.temp_directory_path, self.file_name), 'r') as infile:
            self.assertEqual(self.sentence1, infile.readline())

    def test_history__expect_success(self):
        self.commit_two_revision()

        gm = GitManager(self.temp_directory_path)
        history = gm.history(self.file_name)
        self.assertEqual(2, len(history))
        self.assertEqual(1, history[0][0])
        self.assertEqual(2, history[1][0])
        self.assertLess(history[0][1], history[1][1]) # revision 2's time should be bigger

    def test_history__except_success(self):
        self.commit_two_revision()

        gm = GitManager(self.temp_directory_path)
        self.assertEqual(self.sentence1, gm.content_by_revision(self.file_name, 1))
        self.assertEqual(self.sentence2, gm.content_by_revision(self.file_name, 2))

    def test_history__except_success__with_revision_none(self):
        self.commit_two_revision()

        gm = GitManager(self.temp_directory_path)
        self.assertEqual(self.sentence2, gm.content_by_revision(self.file_name))
