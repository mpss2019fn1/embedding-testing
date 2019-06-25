from src.Result.case_result import CaseResult
from src.Task import AbstractTask


class SimilarityTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "similarity"

    @classmethod
    def task_type(cls):
        from src.Task import TaskType
        return TaskType.SIMILARITY

    def _run(self):
        embedding = self._test_configuration.embedding
        linking = self._test_configuration.entity_linkings
        for line in self._test_set_lines():
            entity1 = linking[line[0]]
            entity2 = linking[line[1]]
            vector1 = embedding[entity1]
            vector2 = embedding[entity2]
            is_expected_similar = line[2].lower() == "true"

            result = self.metric.compute(vector1, vector2)
            is_similar = self.metric.is_better_than_noise(result, embedding)

            yield CaseResult([entity1, entity2], is_expected_similar, result, is_similar == is_expected_similar)
