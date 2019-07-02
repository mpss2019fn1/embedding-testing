from pathlib import Path

from src.FileParsing.ConfigurationFileParsing.task_category_file_parser import TaskCategoryFileParser
from src.FileParsing.ConfigurationFileParsing.task_configuration_file_parser import TaskConfigurationFileParser
from src.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from src.TestConfiguration.test_configuration import TestConfiguration
from src.Testing.TestExecution import TestExecutor
from test.base_test_case import BaseTestCase


class TestTestExecutor(BaseTestCase):

    def setup_method(self):
        super(TestTestExecutor, self).setup_method()
        self.resource_directory = Path(self.resource_directory.absolute(), "test_executor")
        self._test_configuration = self._create_test_configuration()

    def _create_test_configuration(self):
        task_configs = TaskConfigurationFileParser.create_configurations_from_file(
            Path(self.resource_directory, "configuration.yaml"))
        categories = TaskCategoryFileParser.create_categories_from_file(
            Path(self.resource_directory, "configuration.yaml"))
        entity_linking = EntityLinkingFileParser.create_from_file(Path(self.resource_directory, "linking.csv"))
        embedding = EmbeddingFileParser.create_from_file(Path(self.resource_directory, "embedding"))
        return TestConfiguration(embedding, entity_linking, categories, task_configs)

    def test_run(self):
        executor = TestExecutor(self._test_configuration)

        category_results = list(executor.run())

        assert len(category_results) == 2
        assert len(category_results[0].category_results) == 1
        assert len(category_results[1].category_results) == 0
