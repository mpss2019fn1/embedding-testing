from src.Metric.euclidean_distance import EuclideanDistance
from src.Task import TaskMetric


class TestEuclideanDistance:

    def test_calculation_identical(self):
        vector1 = [0, 1]
        vector2 = [0, 1]

        euclidean_distance = EuclideanDistance()

        assert 0 == euclidean_distance.compute(vector1, vector2)

    def test_calculation_not_identical(self):
        vector1 = [0, 1]
        vector2 = [0, 4]

        euclidean_distance = EuclideanDistance()

        assert 9 == euclidean_distance.compute(vector1, vector2)

    def test_configuration_identifier(self):
        assert "euclidean" == EuclideanDistance.configuration_identifier()

    def test_task_metric(self):
        assert TaskMetric.EUCLIDEAN_DISTANCE == EuclideanDistance.task_metric()
