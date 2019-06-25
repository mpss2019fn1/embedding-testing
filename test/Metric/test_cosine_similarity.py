from src.Metric.cosine_similarity import CosineSimilarity


class TestCosineSimilarity:

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
