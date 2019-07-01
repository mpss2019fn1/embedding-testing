from pathlib import Path

from src.FileParsing.ConfigurationFileParsing.task_configuration_file_parser import TaskConfigurationFileParser
from src.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from src.Task.Similarity.cosine_similarity_task import CosineSimilarityTask
from src.TestConfiguration.test_configuration import TestConfiguration
from test.base_test_case import BaseTestCase


class TestCosineSimilarityTask(BaseTestCase):

    def setup_method(self):
        super(TestCosineSimilarityTask, self).setup_method()
        self.resource_directory = Path(self.resource_directory.absolute(), "similarity_task")
        self._test_configuration = self._create_test_configuration()

    def _create_test_configuration(self):
        task_configs = TaskConfigurationFileParser.create_configurations_from_file(
            Path(self.resource_directory, "configuration.yaml"))
        entity_linking = EntityLinkingFileParser.create_from_file(Path(self.resource_directory, "linking.csv"))
        embedding = EmbeddingFileParser.create_from_file(Path(self.resource_directory, "embedding"))
        return TestConfiguration(embedding, entity_linking, [], task_configs)

    def test_run(self):
        task = CosineSimilarityTask("Politicians", Path(self.resource_directory, "politicians.csv"))
        result = task.run(self._test_configuration)

        assert len(result.case_results) == 9
        assert result.pass_rate() == 100
        assert result.execution_duration() > 0

    def test_run_with_failing_tests(self):
        task = CosineSimilarityTask("Politicians", Path(self.resource_directory, "politicians_with_failures.csv"))
        result = task.run(self._test_configuration)

        assert len(result.case_results) == 9
        assert result.pass_rate() == (7 / 9) * 100
        assert result.execution_duration() > 0