import pytest

from src.Task import AnalogyTask, NeighborhoodTask, OutlierDetectionTask, SimilarityTask
from src.Task import TaskType
from test.base_test_case import BaseTestCase


class TestTaskType(BaseTestCase):

    def test_from_string(self):
        assert TaskType.ANALOGY == TaskType.from_string("analogy")
        assert TaskType.NEIGHBORHOOD == TaskType.from_string("neighborhood")
        assert TaskType.OUTLIER_DETECTION == TaskType.from_string("outlier_detection")
        assert TaskType.SIMILARITY == TaskType.from_string("similarity")

    def test_from_string_with_invalid_input_raises_exception(self):
        with pytest.raises(KeyError):
            TaskType.from_string("not_a_valid_task_type")

    def test_value_from_string(self):
        assert AnalogyTask == TaskType.value_from_string("analogy")
        assert NeighborhoodTask == TaskType.value_from_string("neighborhood")
        assert OutlierDetectionTask == TaskType.value_from_string("outlier_detection")
        assert SimilarityTask == TaskType.value_from_string("similarity")

    def test_value_from_string_with_invalid_input_raises_exception(self):
        with pytest.raises(KeyError):
            TaskType.value_from_string("not_a_valid_task_type")
