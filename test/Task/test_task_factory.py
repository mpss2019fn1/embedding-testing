from src.Task import TaskFactory, AnalogyTask, TaskMetric
from test.base_test_case import BaseTestCase


class TestTaskFactory(BaseTestCase):

    def test_extract_name(self):
        config = {"name": "test_name"}
        self.assertEquals("test_name", TaskFactory._extract_name(config))

    def test_extract_name_with_missing_key_raises_exception(self):
        config = {"invalid_label": "test_name"}
        self.assertRaises(KeyError, TaskFactory._extract_name, config)

    def test_extract_test_set(self):
        config = {"test_set": str(self.empty_file.absolute())}
        self.assertEquals(self.empty_file, TaskFactory._extract_test_set(config))

    def test_extract_test_set_with_non_existing_file_raises_exception(self):
        config = {"test_set": "./non-existing-test-set.csv"}
        self.assertRaises(KeyError, TaskFactory._extract_test_set, config)

    def test_create_task_from_configuration(self):
        config = {
            "name": "task-name",
            "type": "analogy",
            "metric": "cosine",
            "test_set": str(self.empty_file.absolute())
        }

        task = TaskFactory.create_task_from_configuration(config)
        self.assertEquals("task-name", task.name)
        self.assertEquals(AnalogyTask, task.__class__)
        self.assertEquals(TaskMetric.COSINE_SIMILARITY, task.metric)
        self.assertEquals(self.empty_file, task.test_set)
