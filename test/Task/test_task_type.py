from src.Task import AnalogyTask, NeighborhoodTask, OutlierDetectionTask, SimilarityTask
from src.Task import TaskType
from test.base_test_case import BaseTestCase


class TestTaskType(BaseTestCase):

    def test_from_string(self):
        self.assertEqual(TaskType.ANALOGY, TaskType.from_string("analogy"))
        self.assertEqual(TaskType.NEIGHBORHOOD, TaskType.from_string("neighborhood"))
        self.assertEqual(TaskType.OUTLIER_DETECTION, TaskType.from_string("outlier_detection"))
        self.assertEqual(TaskType.SIMILARITY, TaskType.from_string("similarity"))

    def test_from_string_with_invalid_input_raises_exception(self):
        self.assertRaises(KeyError, TaskType.from_string, "not_a_valid_task_type")

    def test_value_from_string(self):
        self.assertEqual(AnalogyTask, TaskType.value_from_string("analogy"))
        self.assertEqual(NeighborhoodTask, TaskType.value_from_string("neighborhood"))
        self.assertEqual(OutlierDetectionTask, TaskType.value_from_string("outlier_detection"))
        self.assertEqual(SimilarityTask, TaskType.value_from_string("similarity"))

    def test_value_from_string_with_invalid_input_raises_exception(self):
        self.assertRaises(KeyError, TaskType.value_from_string, "not_a_valid_task_type")
