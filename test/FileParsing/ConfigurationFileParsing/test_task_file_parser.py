import uuid

import pytest

from src.FileParsing.ConfigurationFileParsing.task_file_parser import TaskFileParser
from src.Task.Analogy.analogy_task import AnalogyTask
from test.base_test_case import BaseTestCase


class TestTaskFileParser(BaseTestCase):

    def test_absolute_paths(self):
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

    def test_relative_paths(self):
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

    def test_test_set_does_not_exist(self):
        config = {
            "name": "task-name",
            "type": "analogy",
            "test_set": f"./{uuid.uuid4()}"
        }
        task_file_parser = TaskFileParser(self.empty_file)
        with pytest.raises(KeyError):
            task_file_parser.create_task_from_configuration(config)

    def test_name_is_missing(self):
        config = {
            "type": "analogy",
            "test_set": str(self.empty_file.relative_to(self.test_dir))
        }
        task_file_parser = TaskFileParser(self.empty_file)
        with pytest.raises(KeyError):
            task_file_parser.create_task_from_configuration(config)

    def test_name_is_empty(self):
        config = {
            "name": "",
            "type": "analogy",
            "test_set": str(self.empty_file.relative_to(self.test_dir))
        }
        task_file_parser = TaskFileParser(self.empty_file)
        with pytest.raises(KeyError):
            task_file_parser.create_task_from_configuration(config)

    def test_test_set_missing(self):
        config = {
            "name": "task-name",
            "type": "analogy",
        }
        task_file_parser = TaskFileParser(self.empty_file)
        with pytest.raises(KeyError):
            task_file_parser.create_task_from_configuration(config)

    def test_type_missing(self):
        config = {
            "name": "",
            "test_set": str(self.empty_file.relative_to(self.test_dir))
        }
        task_file_parser = TaskFileParser(self.empty_file)
        with pytest.raises(KeyError):
            task_file_parser.create_task_from_configuration(config)
