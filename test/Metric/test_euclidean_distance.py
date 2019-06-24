from src.Metric.euclidean_distance import EuclideanDistance
from src.Task import TaskMetric


class TestEuclideanDistance:

    def test_calculation_identical(self):
        vector1 = [0, 1]
        vector2 = [0, 1]

        euclidean_distance = EuclideanDistance()

        assert euclidean_distance.compute(vector1, vector2) == 0

    def test_calculation_not_identical(self):
        vector1 = [0, 1]
        vector2 = [0, 4]

        euclidean_distance = EuclideanDistance()

        assert euclidean_distance.compute(vector1, vector2) == 9

    def test_configuration_identifier(self):
        assert EuclideanDistance.configuration_identifier() == "euclidean"

    def test_task_metric(self):
        assert EuclideanDistance.task_metric() == TaskMetric.EUCLIDEAN_DISTANCE