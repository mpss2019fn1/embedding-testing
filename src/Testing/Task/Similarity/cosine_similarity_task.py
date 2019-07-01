from src.Testing.Metric.cosine_similarity import CosineSimilarity
from src.Testing.Task.Similarity.abstract_similarity_task import AbstractSimilarityTask


class CosineSimilarityTask(AbstractSimilarityTask):

    @classmethod
    def configuration_identifier(cls):
        return "cosine_similarity"

    @classmethod
    def task_type(cls):
        from src.Testing.Task.task_type import TaskType
        return TaskType.COSINE_SIMILARITY

    def __init__(self, name, test_set):
        super(CosineSimilarityTask, self).__init__(name, test_set, CosineSimilarity())

    def _stringify_expected_result(self, is_expected_similar):
        expected_result = " > " if is_expected_similar else " <= "
        expected_result += str(self._test_configuration.embedding.random_cosine_noise)

        return expected_result
