import pytest

from src.FileParsing.ConfigurationFileParsing.task_configuration_file_parser import TaskConfigurationFileParser
from src.Task.task_type import TaskType
from test.base_test_case import BaseTestCase


class TestTaskConfigurationFileParser(BaseTestCase):

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
                        type: cosine_neighborhood
                        enabled: false""",
                  file=file_output)

        task_configurations = TaskConfigurationFileParser.create_configurations_from_file(file)
        assert len(task_configurations) == 2

        config = task_configurations[0]
        assert config.task_type == TaskType.ANALOGY
        assert config.enabled

        config = task_configurations[1]
        assert config.task_type == TaskType.COSINE_NEIGHBORHOOD
        assert not config.enabled

    def test_create_configurations_from_file_invalid_boolean_value(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("""
            configuration:
                task_configurations:
                    - task_configuration:
                        type: analogy
                        enabled: true
                    - task_configuration:
                        type: cosine_neighborhood
                        enabled: invalidBool""",
                  file=file_output)

        with pytest.raises(KeyError):
            task_configurations = TaskConfigurationFileParser.create_configurations_from_file(file)

    def test_create_configurations_from_file_invalid_task_type(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("""
            configuration:
                task_configurations:
                    - task_configuration:
                        type: analogy
                        enabled: true
                    - task_configuration:
                        type: invalidTaskType
                        enabled: false""",
                  file=file_output)

        with pytest.raises(KeyError):
            task_configurations = TaskConfigurationFileParser.create_configurations_from_file(file)

    def test_create_configurations_from_file_empty_configurations(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("""
            configuration:
                task_configurations:""",
                  file=file_output)

        task_configurations = TaskConfigurationFileParser.create_configurations_from_file(file)
        assert len(task_configurations) == 0
