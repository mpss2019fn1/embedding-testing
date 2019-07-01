from src.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.Metric.cosine_similarity import CosineSimilarity
from src.Metric.euclidean_distance import EuclideanDistance
from test.base_test_case import BaseTestCase


class TestEuclideanDistance(BaseTestCase):

    def test_calculation_identical(self):
        vector1 = [0, 1]
        vector2 = [0, 1]

        euclidean_distance = EuclideanDistance()

        assert euclidean_distance.compute(vector1, vector2) == 0

    def test_calculation_not_identical(self):
        vector1 = [0, 1]
        vector2 = [0, 4]

        euclidean_distance = EuclideanDistance()

        assert euclidean_distance.compute(vector1, vector2) == 9

    def test_better_than_noise(self):
        embedding_file = self._random_test_file()
        with open(embedding_file, "w+") as file_output:
            print("2 2\n" +
                  "paris 0.0 3.0\n" +
                  "berlin 1.0 0.0", file=file_output)

        embedding = EmbeddingFileParser.create_from_file(embedding_file)
        assert embedding.squared_euclidean_noise == 10.0

        euclidean_distance = EuclideanDistance()

        assert euclidean_distance.is_better_than_noise(9.99, embedding)
        assert not euclidean_distance.is_better_than_noise(10.0, embedding)
        assert not euclidean_distance.is_better_than_noise(10.01, embedding)

    def test_batch_compute(self):
        euclidean_distance = EuclideanDistance()
        vectors = [[0.0, 3.0], [1.0, 0.0]]
        result = euclidean_distance.batch_compute(vectors)
        assert result == 10.0

    def test_equality(self):
        assert EuclideanDistance() == EuclideanDistance()
        assert EuclideanDistance() is not None
        assert not EuclideanDistance() == CosineSimilarity()
