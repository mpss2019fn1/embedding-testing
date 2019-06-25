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
        with open(configuration_file, "r") as stream:
            configuration = yaml.safe_load(stream)
        configuration = configuration[TaskConfigurationFileParser.LABEL_ROOT][
            TaskConfigurationFileParser.LABEL_TASK_CONFIGURATIONS]
        task_configurations = []
        for task_configuration in configuration:
            task_configuration = task_configuration[TaskConfigurationFileParser.LABEL_TASK_CONFIGURATION]
            task_configurations.append(TaskConfigurationFileParser.create_task_configuration(task_configuration))

        return task_configurations

    @staticmethod
    def create_task_configuration(configuration):
        from src.Task import TaskType
        from src.TaskConfiguration import TaskConfiguration

        task_type = TaskType.from_string(configuration[TaskConfigurationFileParser.LABEL_TYPE])
        enabled = TaskConfigurationFileParser._extract_enabled(configuration)

        return TaskConfiguration(task_type, enabled)

    @staticmethod
    def _extract_enabled(configuration):
        enabled = str(configuration[TaskConfigurationFileParser.LABEL_ENABLED]).lower()

        if enabled not in ["true", "false"]:
            logging.error("The provided boolean value for enabled are not valid")
            raise KeyError

        return enabled == "true"
