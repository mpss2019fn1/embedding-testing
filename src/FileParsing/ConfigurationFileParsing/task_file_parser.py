import logging
from pathlib import Path

from src.FileParsing.abstract_file_parser import AbstractFileParser


class TaskFileParser(AbstractFileParser):
    
    LABEL_NAME = "name"
    LABEL_TYPE = "type"
    LABEL_TEST_SET = "test_set"
    LABEL_METRIC = "metric"

    def create_task_from_configuration(self, configuration):
        from src.Task import TaskType, TaskMetric

        name = TaskFileParser._extract_name(configuration)
        task_class = TaskType.value_from_string(configuration[TaskFileParser.LABEL_TYPE])
        metric = TaskMetric.value_from_string(configuration[TaskFileParser.LABEL_METRIC])
        test_set = TaskFileParser._extract_test_set(configuration)

        return task_class(name, test_set, metric)

    def _extract_name(self, configuration):
        name = configuration[TaskFileParser.LABEL_NAME]

        if not name:
            logging.error("The provided task name must not be empty")
            raise KeyError

        return name

    def _extract_test_set(self, configuration):
        test_set = Path(configuration[TaskFileParser.LABEL_TEST_SET])

        if not test_set.is_absolute():
            test_set = Path(self._file_path, test_set)

        if not test_set.exists():
            logging.error(f"The provided test set {test_set} does not exist")
            raise KeyError

        return test_set
