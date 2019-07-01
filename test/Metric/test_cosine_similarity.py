from src.Embedding.embedding import Embedding
from src.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.Metric.cosine_similarity import CosineSimilarity
from src.Metric.euclidean_distance import EuclideanDistance
from test.base_test_case import BaseTestCase


class TestCosineSimilarity(BaseTestCase):

    def test_calculation_identical(self):
        vector1 = [0, 1]
        vector2 = [0, 2]

        cosine_similarity = CosineSimilarity()

        assert cosine_similarity.compute(vector1, vector2) == 1

    def test_calculation_orthogonal(self):
        vector1 = [0, 1]
        vector2 = [1, 0]

        cosine_similarity = CosineSimilarity()

        assert cosine_similarity.compute(vector1, vector2) == 0

    def test_calculation_opposite(self):
        vector1 = [0, 1]
        vector2 = [0, -1]

        cosine_similarity = CosineSimilarity()

        assert cosine_similarity.compute(vector1, vector2) == -1

    def test_is_better_than_noise(self):
        embedding_file = self._random_test_file()
        with open(embedding_file, "w+") as file_output:
            print("2 2\n" +
                  "paris 0.0 3.0\n" +
                  "berlin 1.0 0.0", file=file_output)

        embedding = EmbeddingFileParser.create_from_file(embedding_file)
        assert embedding.random_cosine_noise == 0

        cosine_similarity = CosineSimilarity()

        assert cosine_similarity.is_better_than_noise(1, embedding)
        assert not cosine_similarity.is_better_than_noise(0, embedding)
        assert not cosine_similarity.is_better_than_noise(-1, embedding)

    def test_batch_compute(self):
        cosine_similarity = CosineSimilarity()
        vectors = [[0.0, 4.32], [1.0, 0.0], [0.0, -1312.3], [-4.3, 0.0]]
        result = cosine_similarity.batch_compute(vectors)
        assert result == -(1 / 3)

    def test_equality(self):
        assert CosineSimilarity() == CosineSimilarity()
        assert CosineSimilarity() is not None
        assert not CosineSimilarity() == EuclideanDistance()
