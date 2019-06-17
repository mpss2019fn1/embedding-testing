import shutil
import tempfile
import unittest
import uuid
from pathlib import Path


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.empty_file = Path(self.test_dir, "empty-file")
        self.empty_file.open("w+").close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def _random_test_file(self):
        return Path(self.test_dir, f"{uuid.uuid4()}")
