import pytest

from src.Task.Analogy.analogy_task import AnalogyTask
from src.Task.Neighborhood.cosine_neighborhood_task import CosineNeighborhoodTask
from src.Task.Neighborhood.euclidean_neighborhood_task import EuclideanNeighborhoodTask
from src.Task.OutlierDetection.cosine_outlier_detection_task import CosineOutlierDetectionTask
from src.Task.OutlierDetection.euclidean_outlier_detection_task import EuclideanOutlierDetectionTask
from src.Task.Similarity.cosine_similarity_task import CosineSimilarityTask
from src.Task.Similarity.euclidean_similarity_task import EuclideanSimilarityTask
from src.Task.task_type import TaskType
from test.base_test_case import BaseTestCase


class TestTaskType(BaseTestCase):

    def test_from_string(self):
        assert TaskType.ANALOGY == TaskType.from_string("analogy") == TaskType.ANALOGY
        assert TaskType.from_string("cosine_neighborhood") == TaskType.COSINE_NEIGHBORHOOD
        assert TaskType.from_string("euclidean_neighborhood") == TaskType.EUCLIDEAN_NEIGHBORHOOD
        assert TaskType.from_string("cosine_outlier_detection") == TaskType.COSINE_OUTLIER_DETECTION
        assert TaskType.from_string("euclidean_outlier_detection") == TaskType.EUCLIDEAN_OUTLIER_DETECTION
        assert TaskType.from_string("cosine_similarity") == TaskType.COSINE_SIMILARITY
        assert TaskType.from_string("euclidean_similarity") == TaskType.EUCLIDEAN_SIMILARITY

    def test_from_string_with_invalid_input_raises_exception(self):
        with pytest.raises(KeyError):
            TaskType.from_string("not_a_valid_task_type")

    def test_value_from_string(self):
        assert TaskType.value_from_string("analogy") == AnalogyTask
        assert TaskType.value_from_string("cosine_neighborhood") == CosineNeighborhoodTask
        assert TaskType.value_from_string("euclidean_neighborhood") == EuclideanNeighborhoodTask
        assert TaskType.value_from_string("cosine_outlier_detection") == CosineOutlierDetectionTask
        assert TaskType.value_from_string("euclidean_outlier_detection") == EuclideanOutlierDetectionTask
        assert TaskType.value_from_string("cosine_similarity") == CosineSimilarityTask
        assert TaskType.value_from_string("euclidean_similarity") == EuclideanSimilarityTask

    def test_value_from_string_with_invalid_input_raises_exception(self):
        with pytest.raises(KeyError):
            TaskType.value_from_string("not_a_valid_task_type")
