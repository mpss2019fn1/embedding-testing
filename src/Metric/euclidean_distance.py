from src.Metric.abstract_metric import AbstractMetric


class EuclideanDistance(AbstractMetric):

    @classmethod
    def configuration_identifier(cls):
        return "euclidean"

    @classmethod
    def task_metric(cls):
        from src.Task import TaskMetric
        return TaskMetric.EUCLIDEAN_DISTANCE

    def compute(self, vector1, vector2):
        distance = [(v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)]
        return sum(distance)

    def is_better_than_noise(self, result, embedding):
        return result < embedding.squared_euclidean_noise

    def __eq__(self, other):
        if not isinstance(other, EuclideanDistance):
            return False

        return True
