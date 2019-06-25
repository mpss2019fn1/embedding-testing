from src.Metric.euclidean_distance import EuclideanDistance
from src.Task.Neighborhood.abstract_neighborhood_task import AbstractNeighborhoodTask


class EuclideanNeighborhoodTask(AbstractNeighborhoodTask):

    @classmethod
    def configuration_identifier(cls):
        return "euclidean_neighborhood"

    @classmethod
    def task_type(cls):
        from src.Task.task_type import TaskType
        return TaskType.EUCLIDEAN_NEIGHBORHOOD

    def __init__(self, name, test_set):
        super(EuclideanNeighborhoodTask, self).__init__(name, test_set, EuclideanDistance())
