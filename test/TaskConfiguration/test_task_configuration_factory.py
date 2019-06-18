import pytest

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
        assert 2 == len(task_configurations)

        config = task_configurations[0]
        assert TaskType.ANALOGY == config.task_type
        assert config.enabled

        config = task_configurations[1]
        assert TaskType.NEIGHBORHOOD == config.task_type
        assert not config.enabled

    def test_extract_enabled(self):
        assert TaskConfigurationFactory._extract_enabled({"enabled": "true"})
        assert TaskConfigurationFactory._extract_enabled({"enabled": "TRUE"})

        assert not TaskConfigurationFactory._extract_enabled({"enabled": "false"})
        assert not TaskConfigurationFactory._extract_enabled({"enabled": "FALSE"})

    def test_extract_enabled_with_missing_key_raises_exception(self):
        config = {"invalid_key": "true"}
        with pytest.raises(KeyError):
            TaskConfigurationFactory._extract_enabled(config)

    def test_extract_enabled_with_invalid_value_raises_exception(self):
        config = {"enabled": "not-a-boolean"}
        with pytest.raises(KeyError):
            TaskConfigurationFactory._extract_enabled(config)

    def test_create_task_configuration(self):
        config = {
            "type": "analogy",
            "enabled": "true"
        }

        task_configuration = TaskConfigurationFactory.create_task_configuration(config)

        assert TaskType.ANALOGY == task_configuration.task_type
        assert task_configuration.enabled
