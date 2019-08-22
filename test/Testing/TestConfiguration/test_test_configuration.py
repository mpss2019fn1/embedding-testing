from src.Testing.Task.task_type import TaskType
from src.Testing.TaskConfiguration.task_configuration import TaskConfiguration
from src.Testing.TestConfiguration.test_configuration import TestConfiguration


class TestTestConfiguration:

    def test_task_type_is_enabled(self):
        task_configuration = [
            TaskConfiguration(TaskType.COSINE_SIMILARITY, True),
            TaskConfiguration(TaskType.COSINE_NEIGHBORHOOD, False)
        ]

        # noinspection PyTypeChecker
        test_configuration = TestConfiguration(None, None, None, [], task_configuration)

        assert test_configuration.is_enabled(TaskType.COSINE_SIMILARITY)
        assert not test_configuration.is_enabled(TaskType.COSINE_NEIGHBORHOOD)
