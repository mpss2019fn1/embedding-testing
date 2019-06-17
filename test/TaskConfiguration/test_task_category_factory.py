from src.Task import AnalogyTask, TaskMetric, SimilarityTask
from src.TaskConfiguration import TaskCategoryFactory
from test.base_test_case import BaseTestCase


class TestTaskCategoryFactory(BaseTestCase):

    def test_extract_enabled(self):
        self.assertTrue(TaskCategoryFactory._extract_enabled({"enabled": "true"}))
        self.assertTrue(TaskCategoryFactory._extract_enabled({"enabled": "TRUE"}))

        self.assertFalse(TaskCategoryFactory._extract_enabled({"enabled": "false"}))
        self.assertFalse(TaskCategoryFactory._extract_enabled({"enabled": "FALSE"}))

    def test_extract_enabled_with_missing_key_raises_exception(self):
        config = {"invalid_key": "true"}
        self.assertRaises(KeyError, TaskCategoryFactory._extract_enabled, config)

    def test_extract_enabled_with_invalid_value_raises_exception(self):
        config = {"enabled": "not-a-boolean"}
        self.assertRaises(KeyError, TaskCategoryFactory._extract_enabled, config)

    def test_extract_name(self):
        config = {"name": "test-name"}
        self.assertEqual("test-name", TaskCategoryFactory._extract_name(config))

    def test_extract_name_with_missing_key_raises_exception(self):
        config = {"invalid_key", "test-name"}
        self.assertRaises(KeyError, TaskCategoryFactory._extract_name, config)

    def test_extract_name_with_empty_value_raises_exception(self):
        config = {"name": ""}
        self.assertRaises(KeyError, TaskCategoryFactory._extract_name, config)

    def test_extract_tasks(self):
        config = {
            "tasks": [
                {
                    "task": {
                        "name": "task-name-1",
                        "type": "analogy",
                        "metric": "cosine",
                        "test_set": str(self.empty_file.absolute())
                    }
                },
                {
                    "task": {
                        "name": "task-name-2",
                        "type": "similarity",
                        "metric": "euclidean",
                        "test_set": str(self.empty_file.absolute())
                    }
                }
            ]
        }

        tasks = TaskCategoryFactory._extract_tasks(config)
        self.assertEqual(2, len(tasks))

        task = tasks[0]
        self.assertEqual("task-name-1", task.name)
        self.assertEqual(AnalogyTask, task.__class__)
        self.assertEqual(TaskMetric.COSINE_SIMILARITY, task.metric)
        self.assertEqual(self.empty_file, task.test_set)

        task = tasks[1]
        self.assertEqual("task-name-2", task.name)
        self.assertEqual(SimilarityTask, task.__class__)
        self.assertEqual(TaskMetric.EUCLIDEAN_DISTANCE, task.metric)
        self.assertEqual(self.empty_file, task.test_set)

    def test_extract_tasks_with_empty_list(self):
        config = {
            "tasks": None
        }

        tasks = TaskCategoryFactory._extract_tasks(config)
        self.assertEqual(0, len(tasks))
