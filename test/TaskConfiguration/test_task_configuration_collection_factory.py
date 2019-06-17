import uuid
from pathlib import Path

from src.Task import TaskType
from src.TaskConfiguration.task_configuration_collection_factory import TaskConfigurationCollectionFactory
from test.base_test_case import BaseTestCase


class TestTaskConfigurationCollectionFactory(BaseTestCase):

    def test_create_configurations_from_file(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("""
            configuration:
                task_configurations:
                    - task_configuration:
                        type: analogy
                        enabled: true
                    - task_configuration:
                        type: neighborhood
                        enabled: false""",
                  file=file_output)

        task_configurations = TaskConfigurationCollectionFactory.create_configurations_from_file(file)
        self.assertEqual(2, len(task_configurations.configurations))

        config = task_configurations.configurations[0]
        self.assertEqual(TaskType.ANALOGY, config.task_type)
        self.assertTrue(config.enabled)

        config = task_configurations.configurations[1]
        self.assertEqual(TaskType.NEIGHBORHOOD, config.task_type)
        self.assertFalse(config.enabled)
