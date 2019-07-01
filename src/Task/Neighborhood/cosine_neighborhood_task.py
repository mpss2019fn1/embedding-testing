from src.Metric.cosine_similarity import CosineSimilarity
from src.Task.Neighborhood.abstract_neighborhood_task import AbstractNeighborhoodTask


class CosineNeighborhoodTask(AbstractNeighborhoodTask):

    @classmethod
    def configuration_identifier(cls):
        return "cosine_neighborhood"

    @classmethod
    def task_type(cls):
        from src.Task.task_type import TaskType
        return TaskType.COSINE_NEIGHBORHOOD

    def __init__(self, name, test_set):
        super(CosineNeighborhoodTask, self).__init__(name, test_set, CosineSimilarity())

    def _stringify_expected_result(self, is_expected_similar):
        expected_result = " > " if is_expected_similar else " <= "
        expected_result += str(self._test_configuration.embedding.random_cosine_noise)

        return expected_result
