import pytest

from src.Task import TaskMetric
from test.base_test_case import BaseTestCase


class TestTaskMetric(BaseTestCase):

    def test_from_string(self):
        assert TaskMetric.COSINE_SIMILARITY == TaskMetric.from_string("cosine")
        assert TaskMetric.EUCLIDEAN_DISTANCE == TaskMetric.from_string("euclidean")

    def test_from_string_with_invalid_input_raises_exception(self):
        with pytest.raises(KeyError):
            TaskMetric.from_string("not_a_valid_metric")
