from src.Metric.cosine_similarity import CosineSimilarity
from src.Result.case_result import CaseResult
from src.Task.abstract_task import AbstractTask


class CosineSimilarityTask(AbstractTask):

    def __init__(self, name, test_set):
        super(CosineSimilarityTask, self).__init__(name, test_set)
        self.metric = CosineSimilarity()

    @classmethod
    def configuration_identifier(cls):
        return "cosine_similarity"

    @classmethod
    def task_type(cls):
        from src.Task.task_type import TaskType
        return TaskType.COSINE_SIMILARITY

    def _run(self):
        embedding = self._test_configuration.embedding
        linking = self._test_configuration.entity_linking
        for line in self._test_set_lines():
            entity1 = linking[line[0]]
            entity2 = linking[line[1]]
            is_expected_similar = line[2].lower() == "true"

            result = embedding.word_vectors.similarity(entity1, entity2)
            is_similar = self.metric.is_better_than_noise(result, embedding)

            expected_result = " > " if is_expected_similar else " <= "
            expected_result += str(embedding.random_cosine_noise)

            yield CaseResult([entity1, entity2], expected_result, result, is_similar == is_expected_similar)
