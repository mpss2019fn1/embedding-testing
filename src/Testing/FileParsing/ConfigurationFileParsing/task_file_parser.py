import logging
from pathlib import Path

from src.Testing.EntityLabel.entity_labels import EntityLabels
from src.Testing.FileParsing.abstract_file_parser import AbstractFileParser


class TaskFileParser(AbstractFileParser):
    
    LABEL_NAME = "name"
    LABEL_TYPE = "type"
    LABEL_TEST_SET = "test_set"
    LABEL_METRIC = "metric"

    def __init__(self, configuration_file: Path, entity_labels: EntityLabels):
        super(TaskFileParser, self).__init__(configuration_file)
        self._entity_labels = entity_labels

    def create_task_from_configuration(self, configuration):
        from src.Testing.Task.task_type import TaskType
        task_class = TaskType.value_from_string(configuration[TaskFileParser.LABEL_TYPE])
        name = task_class.configuration_identifier() + ": " + self._extract_name(configuration)
        test_set = self._extract_test_set(configuration)

        return task_class(name, test_set)

    def _extract_name(self, configuration):
        name = configuration[self.LABEL_NAME]

        if not name:
            logging.error("The provided task name must not be empty")
            raise KeyError

        return self._entity_labels[name]

    def _extract_test_set(self, configuration):
        test_set = Path(configuration[self.LABEL_TEST_SET])

        if not test_set.is_absolute():
            test_set = Path(self._file_path.parent, test_set)

        if not test_set.exists():
            logging.error(f"The provided test set {test_set} does not exist")
            raise KeyError

        return test_set
