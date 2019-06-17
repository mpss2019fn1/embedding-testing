import shutil
import tempfile
import unittest
from pathlib import Path


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.empty_file = Path(self.test_dir, "empty-file")
        self.empty_file.open("w+").close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)
