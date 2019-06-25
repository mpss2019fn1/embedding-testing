import pytest

from src.Task.Analogy.analogy_task import AnalogyTask
from src.Task.Neighborhood.neighborhood_task import NeighborhoodTask
from src.Task.OutlierDetection.outlier_detection_task import OutlierDetectionTask
from src.Task.Similarity.cosine_similarity_task import CosineSimilarityTask
from src.Task.task_type import TaskType
from test.base_test_case import BaseTestCase


class TestTaskType(BaseTestCase):

    def test_from_string(self):
        assert TaskType.ANALOGY == TaskType.from_string("analogy") == TaskType.ANALOGY
        assert TaskType.from_string("neighborhood") == TaskType.NEIGHBORHOOD
        assert TaskType.from_string("outlier_detection") == TaskType.OUTLIER_DETECTION
        assert TaskType.from_string("similarity") == TaskType.COSINE_SIMILARITY

    def test_from_string_with_invalid_input_raises_exception(self):
        with pytest.raises(KeyError):
            TaskType.from_string("not_a_valid_task_type")

    def test_value_from_string(self):
        assert TaskType.value_from_string("analogy") == AnalogyTask
        assert TaskType.value_from_string("neighborhood") == NeighborhoodTask
        assert TaskType.value_from_string("outlier_detection") == OutlierDetectionTask
        assert TaskType.value_from_string("similarity") == CosineSimilarityTask

    def test_value_from_string_with_invalid_input_raises_exception(self):
        with pytest.raises(KeyError):
            TaskType.value_from_string("not_a_valid_task_type")
