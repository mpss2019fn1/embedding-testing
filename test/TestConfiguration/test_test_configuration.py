import unittest

from src.Task import TaskType
from src.TaskConfiguration import TaskConfiguration
from src.TestConfiguration.test_configuration import TestConfiguration


class TestTestConfiguration(unittest.TestCase):

    def test_task_type_is_enabled(self):
        task_configuration = [
            TaskConfiguration(TaskType.SIMILARITY, True),
            TaskConfiguration(TaskType.NEIGHBORHOOD, False)
        ]

        test_configuration = TestConfiguration(None, None, [], task_configuration)

        self.assertTrue(test_configuration.is_enabled(TaskType.SIMILARITY))
        self.assertFalse(test_configuration.is_enabled(TaskType.NEIGHBORHOOD))