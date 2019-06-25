import logging

import yaml

from src.FileParsing.abstract_file_parser import AbstractFileParser


class TaskConfigurationFileParser(AbstractFileParser):

    LABEL_ROOT = "configuration"
    LABEL_TASK_CONFIGURATIONS = "task_configurations"
    LABEL_TASK_CONFIGURATION = "task_configuration"
    LABEL_TYPE = "type"
    LABEL_ENABLED = "enabled"

    @staticmethod
    def create_configurations_from_file(configuration_file):
        return TaskConfigurationFileParser(configuration_file).create_configurations()

    def create_configurations(self):
        with open(self._file_path, "r") as stream:
            configuration = yaml.safe_load(stream)
        configuration = configuration[self.LABEL_ROOT][self.LABEL_TASK_CONFIGURATIONS]
        task_configurations = []

        if not configuration:
            return task_configurations

        for task_configuration in configuration:
            task_configuration = task_configuration[self.LABEL_TASK_CONFIGURATION]
            task_configurations.append(self._create_task_configuration(task_configuration))

        return task_configurations

    def _create_task_configuration(self, configuration):
        from src.Task.task_type import TaskType
        from src.TaskConfiguration.task_configuration import TaskConfiguration
        task_type = TaskType.from_string(configuration[self.LABEL_TYPE])
        enabled = self._extract_enabled(configuration)

        return TaskConfiguration(task_type, enabled)

    def _extract_enabled(self, configuration):
        enabled = str(configuration[self.LABEL_ENABLED]).lower()

        if enabled not in ["true", "false"]:
            logging.error("The provided boolean value for enabled are not valid")
            raise KeyError

        return enabled == "true"
