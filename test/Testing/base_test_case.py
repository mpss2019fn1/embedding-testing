import os
import shutil
import tempfile
import uuid
from pathlib import Path


class BaseTestCase:

    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
        self.empty_file = Path(self.test_dir, "empty-file")
        self.empty_file.open("w+").close()
        self.resource_directory = Path(os.path.dirname(os.path.abspath(__file__)), "__resources__")

    def teardown_method(self):
        shutil.rmtree(self.test_dir)

    def _random_test_file(self):
        return Path(self.test_dir, f"{uuid.uuid4()}")
