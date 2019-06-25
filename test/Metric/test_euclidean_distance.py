from src.Metric.euclidean_distance import EuclideanDistance


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