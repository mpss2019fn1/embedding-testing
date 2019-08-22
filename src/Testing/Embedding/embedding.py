import random
from typing import List

from src.Testing.Metric.cosine_similarity import CosineSimilarity
from src.Testing.Metric.euclidean_distance import EuclideanDistance


class Embedding:
    MIN_COSINE_NOISE_ELEMENTS = 100
    COSINE_NOISE_FACTOR = 0.001

    def __init__(self, word_vectors):
        self.word_vectors = word_vectors
        self.word_vectors.init_sims()
        self._squared_euclidean_noises: List[float] = [self._calculate_squared_euclidean_noise(self.word_vectors.vectors)]
        self._random_cosine_noises: List[float] = [self._calculate_random_cosine_noise(self.word_vectors.vectors)]

    def __getitem__(self, word):
        return self.word_vectors[word]

    @property
    def squared_euclidean_noise(self):
        return self._squared_euclidean_noises[-1]

    @property
    def random_cosine_noise(self):
        return self._random_cosine_noises[-1]

    def enter_nesting(self, embedded_tags: List[str]):
        vectors = [self[tag] for tag in embedded_tags]
        next_euclidean_noise: float = self._calculate_squared_euclidean_noise(vectors)
        self._squared_euclidean_noises.append(min(self.squared_euclidean_noise, next_euclidean_noise))
        next_cosine_noise: float = self._calculate_random_cosine_noise(vectors)
        self._random_cosine_noises.append(max(self.random_cosine_noise, next_cosine_noise))

    def exit_nesting(self):
        if len(self._squared_euclidean_noises) > 1:
            self._squared_euclidean_noises.pop()

        if len(self._random_cosine_noises) > 1:
            self._random_cosine_noises.pop()

    @staticmethod
    def _calculate_squared_euclidean_noise(vectors):
        return EuclideanDistance().batch_compute(vectors)

    @staticmethod
    def _calculate_random_cosine_noise(vectors):
        sampled_vectors = Embedding._select_random_vectors(vectors)
        return CosineSimilarity().batch_compute(sampled_vectors)

    @staticmethod
    def _select_random_vectors(vectors):
        size = len(vectors)
        number_of_elements = min(size, max(
            Embedding.MIN_COSINE_NOISE_ELEMENTS, int(size * Embedding.COSINE_NOISE_FACTOR)))
        return random.sample(list(vectors), number_of_elements)
