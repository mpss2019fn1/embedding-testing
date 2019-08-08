import numpy as np

from src.Testing.Metric.abstract_metric import AbstractMetric


class EuclideanDistance(AbstractMetric):

    def compute(self, vector1, vector2):
        distance = [(v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)]
        return sum(distance)

    def batch_compute(self, vectors):
        matrix = np.array(vectors)
        return np.var(matrix, 0, ddof=1).sum() * 2

    def is_better_than_noise(self, result, embedding):
        return result < embedding.squared_euclidean_noise

    def __eq__(self, other):
        if not isinstance(other, EuclideanDistance):
            return False

        return True
