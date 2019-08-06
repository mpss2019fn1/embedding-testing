from scipy.spatial.distance import cdist

from src.Testing.Metric.euclidean_distance import EuclideanDistance
from src.Testing.Task.OutlierDetection.abstract_outlier_detection_task import AbstractOutlierDetectionTask


class EuclideanOutlierDetectionTask(AbstractOutlierDetectionTask):

    @classmethod
    def configuration_identifier(cls):
        return "euclidean_outlier_detection"

    @classmethod
    def task_type(cls):
        from src.Testing.Task.task_type import TaskType
        return TaskType.EUCLIDEAN_OUTLIER_DETECTION

    def __init__(self, name, test_set):
        super(EuclideanOutlierDetectionTask, self).__init__(name, test_set, EuclideanDistance())

    def _identify_outlier(self, embedding):
        from numpy import vstack

        vectors = vstack(embedding.word_vectors.word_vec(word) for word in self._current_group)
        centroid = vectors.mean(axis=0)
        distances = cdist([centroid], vectors)
        return sorted(zip(distances[0], self._current_group), reverse=True)[0][1]
