class Embeddings:

    def __init__(self, word_vectors):
        self._word_vectors = word_vectors

    def __getitem__(self, word):
        return self._word_vectors[word]
