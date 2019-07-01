from gensim import matutils
from numpy import vstack, float32, dot

from src.Metric.cosine_similarity import CosineSimilarity
from src.Task.OutlierDetection.abstract_outlier_detection_task import AbstractOutlierDetectionTask


class CosineOutlierDetectionTask(AbstractOutlierDetectionTask):

    @classmethod
    def configuration_identifier(cls):
        return "cosine_outlier_detection"

    @classmethod
    def task_type(cls):
        from src.Task.task_type import TaskType
        return TaskType.COSINE_OUTLIER_DETECTION

    def __init__(self, name, test_set):
        super(CosineOutlierDetectionTask, self).__init__(name, test_set, CosineSimilarity())

    def _identify_outlier(self, embedding):
        vectors = vstack(embedding.word_vectors.word_vec(word, use_norm=True) for word in self._current_group)\
            .astype(float32)
        mean = matutils.unitvec(vectors.mean(axis=0)).astype(float32)
        similarities = dot(vectors, mean)
        return sorted(zip(similarities, self._current_group))[0][1]
