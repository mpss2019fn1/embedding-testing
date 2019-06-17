import logging


class TaskConfigurationFactory:

    LABEL_TYPE = "type"
    LABEL_ENABLED = "enabled"

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
