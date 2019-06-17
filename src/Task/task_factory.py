import logging
from pathlib import Path


class TaskFactory:
    
    LABEL_NAME = "name"
    LABEL_TYPE = "type"
    LABEL_TEST_SET = "test_set"
    LABEL_METRIC = "metric"

    @staticmethod
    def create_task_from_configuration(configuration):
        from src.Task import TaskType, TaskMetric

        name = TaskFactory._extract_name(configuration)
        task_class = TaskType.from_string(configuration[TaskFactory.LABEL_TYPE])
        metric = TaskMetric.from_string(configuration[TaskFactory.LABEL_METRIC])
        test_set = TaskFactory._extract_test_set(configuration)

        return task_class(name, test_set, metric)

    @staticmethod
    def _extract_name(configuration):
        name = configuration[TaskFactory.LABEL_NAME]

        if not name:
            logging.error("The provided task name must not be empty")
            raise KeyError

        return name

    @staticmethod
    def _extract_test_set(configuration):
        test_set = Path(configuration[TaskFactory.LABEL_TEST_SET])

        if not test_set.exists():
            logging.error(f"The provided test set {test_set} does not exist")
            raise KeyError

        return test_set
