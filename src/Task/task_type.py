import logging
from enum import Enum

from src.Task.Analogy.analogy_task import AnalogyTask
from src.Task.Neighborhood.cosine_neighborhood_task import CosineNeighborhoodTask
from src.Task.Neighborhood.euclidean_neighborhood_task import EuclideanNeighborhoodTask
from src.Task.OutlierDetection.outlier_detection_task import OutlierDetectionTask
from src.Task.Similarity.cosine_similarity_task import CosineSimilarityTask
from src.Task.Similarity.euclidean_similarity_task import EuclideanSimilarityTask


class TaskType(Enum):
    ANALOGY = AnalogyTask
    COSINE_NEIGHBORHOOD = CosineNeighborhoodTask
    EUCLIDEAN_NEIGHBORHOOD = EuclideanNeighborhoodTask
    OUTLIER_DETECTION = OutlierDetectionTask
    COSINE_SIMILARITY = CosineSimilarityTask
    EUCLIDEAN_SIMILARITY = EuclideanSimilarityTask

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
