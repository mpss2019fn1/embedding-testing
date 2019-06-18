import pytest

from src.Task import TaskFactory, AnalogyTask, TaskMetric
from test.base_test_case import BaseTestCase


class TestTaskFactory(BaseTestCase):

    def test_extract_name(self):
        config = {"name": "test_name"}
        assert "test_name" == TaskFactory._extract_name(config)

    def test_extract_name_with_missing_key_raises_exception(self):
        config = {"invalid_label": "test_name"}
        with pytest.raises(KeyError):
            TaskFactory._extract_name(config)

    def test_extract_test_set(self):
        config = {"test_set": str(self.empty_file.absolute())}
        assert self.empty_file == TaskFactory._extract_test_set(config)

    def test_extract_test_set_with_non_existing_file_raises_exception(self):
        config = {"test_set": "./non-existing-test-set.csv"}
        with pytest.raises(KeyError):
            TaskFactory._extract_test_set(config)

    def test_create_task_from_configuration(self):
        config = {
            "name": "task-name",
            "type": "analogy",
            "metric": "cosine",
            "test_set": str(self.empty_file.absolute())
        }

        task = TaskFactory.create_task_from_configuration(config)
        assert "task-name" == task.name
        assert AnalogyTask == task.__class__
        assert TaskMetric.COSINE_SIMILARITY == task.metric
        assert self.empty_file == task.test_set
