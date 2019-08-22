from pathlib import Path

from src.Testing.EntityLabel.entity_labels import EntityLabels
from src.Testing.FileParsing.ConfigurationFileParsing.task_configuration_file_parser import TaskConfigurationFileParser
from src.Testing.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.Testing.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from src.Testing.Task.OutlierDetection.euclidean_outlier_detection_task import EuclideanOutlierDetectionTask
from src.Testing.Task.task_type import TaskType
from src.Testing.TaskConfiguration.task_configuration import TaskConfiguration
from src.Testing.TestConfiguration.test_configuration import TestConfiguration
from test.Testing.base_test_case import BaseTestCase


class TestEuclideanOutlierDetection(BaseTestCase):

    def setup_method(self):
        super(TestEuclideanOutlierDetection, self).setup_method()
        self.resource_directory = Path(self.resource_directory.absolute(), "outlier_detection_task")
        self._test_configuration = self._create_test_configuration()

    def _create_test_configuration(self):
        task_configs = TaskConfigurationFileParser.create_configurations_from_file(
            Path(self.resource_directory, "configuration.yaml"))
        entity_linking = EntityLinkingFileParser.create_from_file(Path(self.resource_directory, "linking.csv"))
        embedding = EmbeddingFileParser.create_from_file(Path(self.resource_directory, "embedding"))
        entity_labels = EntityLabels()
        return TestConfiguration(embedding, entity_linking, entity_labels, [], task_configs)

    def test_run(self):
        task = EuclideanOutlierDetectionTask("Politicians", Path(self.resource_directory, "politicians.csv"))
        result = task.run(self._test_configuration)

        assert len(result.case_results) == 2
        assert result.pass_rate() == 100
        assert result.execution_duration() > 0

    def test_run_with_failing_tests(self):
        task = EuclideanOutlierDetectionTask("Politicians",
                                             Path(self.resource_directory, "politicians_with_failures.csv"))
        result = task.run(self._test_configuration)

        assert len(result.case_results) == 2
        assert result.pass_rate() == (1 / 2) * 100
        assert result.execution_duration() > 0

    def test_run_with_too_few_elements_in_group(self):
        task = EuclideanOutlierDetectionTask("Politicians",
                                             Path(self.resource_directory, "politicians_too_few_elements.csv"))
        result = task.run(self._test_configuration)

        assert len(result.case_results) == 2
        assert result.pass_rate() == (1 / 2) * 100
        assert result.execution_duration() > 0

    def test_run_disabled_returns_empty_result(self):
        # noinspection PyTypeChecker
        test_configuration = TestConfiguration({}, {}, EntityLabels(), {}, [TaskConfiguration(TaskType.EUCLIDEAN_OUTLIER_DETECTION, False)])
        task = EuclideanOutlierDetectionTask("Disabled Task", Path())

        result = task.run(test_configuration)

        assert result.is_finalized()
        assert not result.has_results()
