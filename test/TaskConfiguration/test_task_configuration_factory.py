from src.Task import TaskType
from src.TaskConfiguration import TaskConfigurationFactory
from test.base_test_case import BaseTestCase


class TestTaskConfigurationFactory(BaseTestCase):

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

        task_configurations = TaskConfigurationFactory.create_configurations_from_file(file)
        self.assertEqual(2, len(task_configurations))

        config = task_configurations[0]
        self.assertEqual(TaskType.ANALOGY, config.task_type)
        self.assertTrue(config.enabled)

        config = task_configurations[1]
        self.assertEqual(TaskType.NEIGHBORHOOD, config.task_type)
        self.assertFalse(config.enabled)

    def test_extract_enabled(self):
        self.assertTrue(TaskConfigurationFactory._extract_enabled({"enabled": "true"}))
        self.assertTrue(TaskConfigurationFactory._extract_enabled({"enabled": "TRUE"}))

        self.assertFalse(TaskConfigurationFactory._extract_enabled({"enabled": "false"}))
        self.assertFalse(TaskConfigurationFactory._extract_enabled({"enabled": "FALSE"}))

    def test_extract_enabled_with_missing_key_raises_exception(self):
        config = {"invalid_key": "true"}
        self.assertRaises(KeyError, TaskConfigurationFactory._extract_enabled, config)

    def test_extract_enabled_with_invalid_value_raises_exception(self):
        config = {"enabled": "not-a-boolean"}
        self.assertRaises(KeyError, TaskConfigurationFactory._extract_enabled, config)

    def test_create_task_configuration(self):
        config = {
            "type": "analogy",
            "enabled": "true"
        }

        task_configuration = TaskConfigurationFactory.create_task_configuration(config)

        self.assertEqual(TaskType.ANALOGY, task_configuration.task_type)
        self.assertEqual(True, task_configuration.enabled)
