from src.Task.task_type import TaskType
from src.TaskConfiguration.task_configuration import TaskConfiguration
from src.TestConfiguration.test_configuration import TestConfiguration


class TestTestConfiguration:

    def test_task_type_is_enabled(self):
        task_configuration = [
            TaskConfiguration(TaskType.COSINE_SIMILARITY, True),
            TaskConfiguration(TaskType.COSINE_NEIGHBORHOOD, False)
        ]

        # noinspection PyTypeChecker
        test_configuration = TestConfiguration(None, None, [], task_configuration)

        assert test_configuration.is_enabled(TaskType.COSINE_SIMILARITY)
        assert not test_configuration.is_enabled(TaskType.COSINE_NEIGHBORHOOD)
