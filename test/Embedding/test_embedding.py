from src.Embedding.embedding_factory import EmbeddingFactory
from test.base_test_case import BaseTestCase


class TestEmbedding(BaseTestCase):

    def test_squared_euclidean_noise(self):
        embedding_file = self._random_test_file()
        with open(embedding_file, "w+") as file_output:
            print("2 2\n" +
                  "paris 0.0 3.0\n" +
                  "berlin 0.0 0.0", file=file_output)

        embedding = EmbeddingFactory.create_from_file(embedding_file)
        assert embedding.squared_euclidean_noise == 9

    def test_random_cosine_noise(self):
        embedding_file = self._random_test_file()
        with open(embedding_file, "w+") as file_output:
            print("2 2\n" +
                  "paris 0.0 3.0\n" +
                  "berlin 1.0 0.0", file=file_output)

        embedding = EmbeddingFactory.create_from_file(embedding_file)
        assert embedding.random_cosine_noise == 0
