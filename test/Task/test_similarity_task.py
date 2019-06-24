from pathlib import Path

from src.Embedding.embedding_factory import EmbeddingFactory
from src.EntityLinking.entity_linkings_factory import EntityLinkingsFactory
from src.Metric.cosine_similarity import CosineSimilarity
from src.Task import SimilarityTask
from src.TaskConfiguration import TaskConfigurationFactory
from src.TestConfiguration.test_configuration import TestConfiguration
from test.base_test_case import BaseTestCase


class TestSimilarityTask(BaseTestCase):

    def setup_method(self):
        super(TestSimilarityTask, self).setup_method()
        self.resource_directory = Path(self.resource_directory.absolute(), "similarity_task")
        self._test_configuration = self._create_test_configuration()

    def _create_test_configuration(self):
        task_configs = TaskConfigurationFactory.create_configurations_from_file(
            Path(self.resource_directory, "configuration.yaml"))
        entity_linking = EntityLinkingsFactory.create_from_file(Path(self.resource_directory, "linking.csv"))
        embedding = EmbeddingFactory.create_from_file(Path(self.resource_directory, "embedding"))
        return TestConfiguration(embedding, entity_linking, [], task_configs)

    def test_run(self):
        similarity_task = SimilarityTask("Politicians", Path(self.resource_directory, "politicians.csv"),
                                         CosineSimilarity())
        task_result = similarity_task.run(self._test_configuration)

        assert 9 == len(task_result.case_results)
        assert 100 == task_result.pass_rate()
        assert 0 < task_result.execution_duration()

    def test_run_with_failing_tests(self):
        similarity_task = SimilarityTask("Politicians", Path(self.resource_directory, "politicians_with_failures.csv"),
                                         CosineSimilarity())
        task_result = similarity_task.run(self._test_configuration)

        assert 9 == len(task_result.case_results)
        assert (7 / 9) * 100 == task_result.pass_rate()
        assert 0 < task_result.execution_duration()
