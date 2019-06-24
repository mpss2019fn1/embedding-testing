from pathlib import Path

from src.Embedding.embedding_factory import EmbeddingFactory
from src.EntityLinking.entity_linkings_factory import EntityLinkingsFactory
from src.Metric.cosine_similarity import CosineSimilarity
from src.Task import AnalogyTask
from src.TaskConfiguration import TaskConfigurationFactory
from src.TestConfiguration.test_configuration import TestConfiguration
from test.base_test_case import BaseTestCase


class TestAnalogyTask(BaseTestCase):

    def setup_method(self):
        super(TestAnalogyTask, self).setup_method()
        self.resource_directory = Path(self.resource_directory.absolute(), "analogy_task")
        self._test_configuration = self._create_test_configuration()

    def _create_test_configuration(self):
        task_configs = TaskConfigurationFactory.create_configurations_from_file(
            Path(self.resource_directory, "configuration.yaml"))
        entity_linking = EntityLinkingsFactory.create_from_file(Path(self.resource_directory, "linking.csv"))
        embedding = EmbeddingFactory.create_from_file(Path(self.resource_directory, "embedding"))
        return TestConfiguration(embedding, entity_linking, [], task_configs)

    def test_run(self):
        task = AnalogyTask("Capitals", Path(self.resource_directory, "capitals.csv"), CosineSimilarity())
        result = task.run(self._test_configuration)

        assert 3 == len(result.case_results)
        assert 100 == result.pass_rate()
        assert 0 < result.execution_duration()

    def test_run_with_failing_tests(self):
        task = AnalogyTask("Capitals", Path(self.resource_directory, "capitals_with_failures.csv"), CosineSimilarity())
        result = task.run(self._test_configuration)

        assert 3 == len(result.case_results)
        assert (1 / 3) * 100 == result.pass_rate()
        assert 0 < result.execution_duration()
