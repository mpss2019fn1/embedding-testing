import pytest

from src.Task import TaskType
from src.TaskConfiguration import TaskConfigurationFileParser
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

        task_configurations = TaskConfigurationFileParser.create_configurations_from_file(file)
        assert len(task_configurations) == 2

        config = task_configurations[0]
        assert config.task_type == TaskType.ANALOGY
        assert config.enabled

        config = task_configurations[1]
        assert config.task_type == TaskType.NEIGHBORHOOD
        assert not config.enabled

    def test_extract_enabled(self):
        assert TaskConfigurationFileParser._extract_enabled({"enabled": "true"})
        assert TaskConfigurationFileParser._extract_enabled({"enabled": "TRUE"})

        assert not TaskConfigurationFileParser._extract_enabled({"enabled": "false"})
        assert not TaskConfigurationFileParser._extract_enabled({"enabled": "FALSE"})

    def test_extract_enabled_with_missing_key_raises_exception(self):
        config = {"invalid_key": "true"}
        with pytest.raises(KeyError):
            TaskConfigurationFileParser._extract_enabled(config)

    def test_extract_enabled_with_invalid_value_raises_exception(self):
        config = {"enabled": "not-a-boolean"}
        with pytest.raises(KeyError):
            TaskConfigurationFileParser._extract_enabled(config)

    def test_create_task_configuration(self):
        config = {
            "type": "analogy",
            "enabled": "true"
        }

        task_configuration = TaskConfigurationFileParser.create_task_configuration(config)

        assert task_configuration.task_type == TaskType.ANALOGY
        assert task_configuration.enabled
