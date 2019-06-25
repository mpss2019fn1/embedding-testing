from pathlib import Path

from src.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from src.Metric.cosine_similarity import CosineSimilarity
from src.Task import AnalogyTask
from src.TaskConfiguration import TaskConfigurationFileParser
from src.TestConfiguration.test_configuration import TestConfiguration
from test.base_test_case import BaseTestCase


class TestAnalogyTask(BaseTestCase):

    def setup_method(self):
        super(TestAnalogyTask, self).setup_method()
        self.resource_directory = Path(self.resource_directory.absolute(), "analogy_task")
        self._test_configuration = self._create_test_configuration()

    def _create_test_configuration(self):
        task_configs = TaskConfigurationFileParser.create_configurations_from_file(
            Path(self.resource_directory, "configuration.yaml"))
        entity_linking = EntityLinkingFileParser.create_from_file(Path(self.resource_directory, "linking.csv"))
        embedding = EmbeddingFileParser.create_from_file(Path(self.resource_directory, "embedding"))
        return TestConfiguration(embedding, entity_linking, [], task_configs)

    def test_run(self):
        task = AnalogyTask("Capitals", Path(self.resource_directory, "capitals.csv"), CosineSimilarity())
        result = task.run(self._test_configuration)

        assert len(result.case_results) == 3
        assert result.pass_rate() == 100
        assert result.execution_duration() > 0

    def test_run_with_failing_tests(self):
        task = AnalogyTask("Capitals", Path(self.resource_directory, "capitals_with_failures.csv"), CosineSimilarity())
        result = task.run(self._test_configuration)

        assert len(result.case_results) == 3
        assert result.pass_rate() == (1 / 3) * 100
        assert result.execution_duration() > 0
