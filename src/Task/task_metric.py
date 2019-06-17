import logging
from enum import Enum


class TaskMetric(Enum):
    COSINE_SIMILARITY = "cosine"
    EUCLIDEAN_DISTANCE = "euclidean"

    @classmethod
    def from_string(cls, metric):
        for member in TaskMetric:
            if member.value == metric:
                return member
        logging.error(f"Unsupported metric type {metric}")
        raise KeyError
