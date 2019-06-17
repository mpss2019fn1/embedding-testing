import yaml

from src.TaskConfiguration.task_configuration_collection import TaskConfigurationCollection
from src.TaskConfiguration import TaskConfigurationFactory


class TaskConfigurationCollectionFactory:
    LABEL_ROOT = "configuration"
    LABEL_TASK_CONFIGURATIONS = "task_configurations"
    LABEL_TASK_CONFIGURATION = "task_configuration"

    @staticmethod
    def create_configurations_from_file(configuration_file):
        with open(configuration_file, "r") as stream:
            configuration = yaml.safe_load(stream)
        configuration = configuration[TaskConfigurationCollectionFactory.LABEL_ROOT][
            TaskConfigurationCollectionFactory.LABEL_TASK_CONFIGURATIONS]
        task_configurations = []
        for task_configuration in configuration:
            task_configuration = task_configuration[TaskConfigurationCollectionFactory.LABEL_TASK_CONFIGURATION]
            task_configurations.append(TaskConfigurationFactory.create_task_configuration(task_configuration))

        return TaskConfigurationCollection(task_configurations)
