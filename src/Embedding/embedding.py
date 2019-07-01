import random

from src.Metric.cosine_similarity import CosineSimilarity
from src.Metric.euclidean_distance import EuclideanDistance


class Embedding:
    MIN_COSINE_NOISE_ELEMENTS = 100
    COSINE_NOISE_FACTOR = 0.001

    def __init__(self, word_vectors):
        self.word_vectors = word_vectors
        self.squared_euclidean_noise = self._calculate_squared_euclidean_noise()
        self.random_cosine_noise = self._calculate_random_cosine_noise()

    def __getitem__(self, word):
        return self.word_vectors[word]

    def _calculate_squared_euclidean_noise(self):
        return EuclideanDistance().batch_compute(self.word_vectors.vectors)

    def _calculate_random_cosine_noise(self):
        vectors = self._select_random_vectors()
        return CosineSimilarity().batch_compute(vectors)

    def _select_random_vectors(self):
        size = len(self.word_vectors.vectors)
        number_of_elements = min(size, max(
            Embedding.MIN_COSINE_NOISE_ELEMENTS, int(size * Embedding.COSINE_NOISE_FACTOR)))
        return random.sample(list(self.word_vectors.vectors), number_of_elements)
