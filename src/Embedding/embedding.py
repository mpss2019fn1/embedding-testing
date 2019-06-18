import numpy as np


class Embedding:

    def __init__(self, word_vectors):
        self._word_vectors = word_vectors
        self.squared_euclidean_noise = self._calculate_squared_euclidean_noise()

    def __getitem__(self, word):
        return self._word_vectors[word]

    def _calculate_squared_euclidean_noise(self):
        matrix = np.array(self._word_vectors.vectors)
        return np.var(matrix, 0, ddof=1).sum() * 2
