import logging

import yaml


class TaskConfigurationFactory:

    LABEL_ROOT = "configuration"
    LABEL_TASK_CONFIGURATIONS = "task_configurations"
    LABEL_TASK_CONFIGURATION = "task_configuration"
    LABEL_TYPE = "type"
    LABEL_ENABLED = "enabled"

    @staticmethod
    def create_configurations_from_file(configuration_file):
        with open(configuration_file, "r") as stream:
            configuration = yaml.safe_load(stream)
        configuration = configuration[TaskConfigurationFactory.LABEL_ROOT][
            TaskConfigurationFactory.LABEL_TASK_CONFIGURATIONS]
        task_configurations = []
        for task_configuration in configuration:
            task_configuration = task_configuration[TaskConfigurationFactory.LABEL_TASK_CONFIGURATION]
            task_configurations.append(TaskConfigurationFactory.create_task_configuration(task_configuration))

        return task_configurations

    @staticmethod
    def create_task_configuration(configuration):
        from src.Task import TaskType
        from src.TaskConfiguration import TaskConfiguration

        task_type = TaskType.from_string(configuration[TaskConfigurationFactory.LABEL_TYPE])
        enabled = TaskConfigurationFactory._extract_enabled(configuration)

        return TaskConfiguration(task_type, enabled)

    @staticmethod
    def _extract_enabled(configuration):
        enabled = str(configuration[TaskConfigurationFactory.LABEL_ENABLED]).lower()

        if enabled not in ["true", "false"]:
            logging.error("The provided boolean value for enabled are not valid")
            raise KeyError

        return enabled == "true"
