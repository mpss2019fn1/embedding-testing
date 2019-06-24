import logging
from enum import Enum

from src.Metric.cosine_similarity import CosineSimilarity
from src.Metric.euclidean_distance import EuclideanDistance


class TaskMetric(Enum):
    COSINE_SIMILARITY = CosineSimilarity()
    EUCLIDEAN_DISTANCE = EuclideanDistance()

    @classmethod
    def from_string(cls, task_metric):
        for member in TaskMetric:
            if member.value.configuration_identifier() == task_metric:
                return member
        logging.error(f"Unable to find MetricType {task_metric}")
        raise KeyError

    @classmethod
    def value_from_string(cls, task_metric):
        return TaskMetric.from_string(task_metric).value
