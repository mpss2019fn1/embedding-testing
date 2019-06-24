import logging
from enum import Enum

from src.Task import AnalogyTask, NeighborhoodTask, OutlierDetectionTask, SimilarityTask


class TaskType(Enum):
    ANALOGY = AnalogyTask
    NEIGHBORHOOD = NeighborhoodTask
    OUTLIER_DETECTION = OutlierDetectionTask
    SIMILARITY = SimilarityTask

    @classmethod
    def from_string(cls, task_type):
        for member in TaskType:
            if member.value.configuration_identifier() == task_type:
                return member
        logging.error(f"Unable to find TaskType {task_type}")
        raise KeyError

    @classmethod
    def value_from_string(cls, task_type):
        return TaskType.from_string(task_type).value
