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
