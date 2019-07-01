from scipy.spatial.distance import cosine

from src.Metric.abstract_metric import AbstractMetric


class CosineSimilarity(AbstractMetric):

    def compute(self, vector1, vector2):
        return 1 - cosine(vector1, vector2)

    def batch_compute(self, vectors):
        running_average = 0
        number_of_comparisons = len(vectors) * (len(vectors) - 1) / 2
        for a in range(0, len(vectors)):
            vector1 = vectors[a]
            for b in range(a + 1, len(vectors)):
                vector2 = vectors[b]
                running_average += self.compute(vector1, vector2) / number_of_comparisons
        return running_average

    def is_better_than_noise(self, result, embedding):
        return result > embedding.random_cosine_noise

    def __eq__(self, other):
        if not isinstance(other, CosineSimilarity):
            return False

        return True
