import random

import numpy as np

from src.Metric.cosine_similarity import CosineSimilarity


class Embedding:
    MIN_COSINE_NOISE_ELEMENTS = 100
    COSINE_NOISE_FACTOR = 0.001

    def __init__(self, word_vectors):
        self._word_vectors = word_vectors
        self.squared_euclidean_noise = self._calculate_squared_euclidean_noise()
        self.random_cosine_noise = self._calculate_random_cosine_noise()

    def __getitem__(self, word):
        return self._word_vectors[word]

    def _calculate_squared_euclidean_noise(self):
        matrix = np.array(self._word_vectors.vectors)
        return np.var(matrix, 0, ddof=1).sum() * 2

    def _calculate_random_cosine_noise(self):
        sample = self._select_random_elements()
        cosine_similarity = CosineSimilarity()
        running_average = 0
        number_of_comparisons = len(sample) * (len(sample) - 1)
        for a, vector1 in enumerate(sample):
            for b, vector2 in enumerate(sample):
                if a == b:
                    continue
                running_average += cosine_similarity.compute(vector1, vector2) / number_of_comparisons
        return running_average

    def _select_random_elements(self):
        size = len(self._word_vectors.vectors)
        number_of_elements = min(size, max(
            Embedding.MIN_COSINE_NOISE_ELEMENTS, int(size * Embedding.COSINE_NOISE_FACTOR)))
        return random.sample(list(self._word_vectors.vectors), number_of_elements)
