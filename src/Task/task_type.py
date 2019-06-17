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
                return member.value
        logging.error(f"Unable to find TestTaskType {task_type}")
        raise KeyError
