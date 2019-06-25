import uuid

import pytest

from src.FileParsing.ConfigurationFileParsing.task_file_parser import TaskFileParser
from src.Task.Analogy.analogy_task import AnalogyTask
from test.base_test_case import BaseTestCase


class TestTaskFileParser(BaseTestCase):

    def test_create_task_from_configuration_with_absolute_paths(self):
        config = {
            "name": "task-name",
            "type": "analogy",
            "test_set": str(self.empty_file.absolute())
        }
        task_file_parser = TaskFileParser(self.empty_file)
        task = task_file_parser.create_task_from_configuration(config)
        assert task.name == "task-name"
        assert task.__class__ == AnalogyTask
        assert task.test_set == self.empty_file

    def test_create_task_from_configuration_with_relative_paths(self):
        config = {
            "name": "task-name",
            "type": "analogy",
            "test_set": str(self.empty_file.relative_to(self.test_dir))
        }
        task_file_parser = TaskFileParser(self.empty_file)
        task = task_file_parser.create_task_from_configuration(config)
        assert task.name == "task-name"
        assert task.__class__ == AnalogyTask
        assert task.test_set == self.empty_file

    def test_create_task_from_configuration_test_set_missing(self):
        config = {
            "name": "task-name",
            "type": "analogy",
            "test_set": f"./{uuid.uuid4()}"
        }
        task_file_parser = TaskFileParser(self.empty_file)
        with pytest.raises(KeyError):
            task = task_file_parser.create_task_from_configuration(config)
