from scipy.spatial.distance import cosine

from src.Metric.abstract_metric import AbstractMetric


class CosineSimilarity(AbstractMetric):

    def compute(self, vector1, vector2):
        return 1 - cosine(vector1, vector2)

    def is_better_than_noise(self, result, embedding):
        return result > embedding.random_cosine_noise

    def __eq__(self, other):
        if not isinstance(other, CosineSimilarity):
            return False

        return True
