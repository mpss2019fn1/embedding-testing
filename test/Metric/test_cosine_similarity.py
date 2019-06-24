from src.Metric.cosine_similarity import CosineSimilarity
from src.Task import TaskMetric


class TestCosineSimilarity:

    def test_calculation_identical(self):
        vector1 = [0, 1]
        vector2 = [0, 2]

        cosine_similarity = CosineSimilarity()

        assert 1 == cosine_similarity.compute(vector1, vector2)

    def test_calculation_orthogonal(self):
        vector1 = [0, 1]
        vector2 = [1, 0]

        cosine_similarity = CosineSimilarity()

        assert 0 == cosine_similarity.compute(vector1, vector2)

    def test_calculation_opposite(self):
        vector1 = [0, 1]
        vector2 = [0, -1]

        cosine_similarity = CosineSimilarity()

        assert -1 == cosine_similarity.compute(vector1, vector2)

    def test_configuration_identifier(self):
        assert "cosine" == CosineSimilarity.configuration_identifier()

    def test_task_metric(self):
        assert TaskMetric.COSINE_SIMILARITY == CosineSimilarity.task_metric()
