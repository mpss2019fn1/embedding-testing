from src.Testing.Metric.euclidean_distance import EuclideanDistance
from src.Testing.Task.Neighborhood.abstract_neighborhood_task import AbstractNeighborhoodTask


class EuclideanNeighborhoodTask(AbstractNeighborhoodTask):

    @classmethod
    def configuration_identifier(cls):
        return "euclidean_neighborhood"

    @classmethod
    def task_type(cls):
        from src.Testing.Task.task_type import TaskType
        return TaskType.EUCLIDEAN_NEIGHBORHOOD

    def __init__(self, name, test_set):
        super(EuclideanNeighborhoodTask, self).__init__(name, test_set, EuclideanDistance())

    def _stringify_expected_result(self, is_expected_similar):
        expected_result = " < " if is_expected_similar else " >= "
        expected_result += '%06.4f' % self._test_configuration.embedding.squared_euclidean_noise

        return expected_result
