from src.Task import AnalogyTask, NeighborhoodTask, OutlierDetectionTask, SimilarityTask
from src.Task import TaskType
from test.base_test_case import BaseTestCase


class TestTaskType(BaseTestCase):

    def test_from_string(self):
        self.assertEquals(AnalogyTask, TaskType.from_string("analogy"))
        self.assertEquals(NeighborhoodTask, TaskType.from_string("neighborhood"))
        self.assertEquals(OutlierDetectionTask, TaskType.from_string("outlier_detection"))
        self.assertEquals(SimilarityTask, TaskType.from_string("similarity"))

    def test_from_string_with_invalid_input_raises_exception(self):
        self.assertRaises(KeyError, TaskType.from_string, "not_a_valid_task_type")
