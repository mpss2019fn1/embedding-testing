from src.Result.case_result import CaseResult
from src.Task import AbstractTask


class AnalogyTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "analogy"

    @classmethod
    def task_type(cls):
        from src.Task import TaskType
        return TaskType.ANALOGY

    def _run(self):
        embedding = self._test_configuration.embedding
        linking = self._test_configuration.entity_linkings
        for indexA, lineA in enumerate(self._test_set_lines()):
            for indexB, lineB in enumerate(self._test_set_lines()):
                if indexA >= indexB:
                    continue

                entity_a1 = linking[lineA[0]]
                entity_a2 = linking[lineA[1]]
                vector_a1 = embedding[entity_a1]
                vector_a2 = embedding[entity_a2]
                vector1 = vector_a2 - vector_a1

                entity_b1 = linking[lineB[0]]
                entity_b2 = linking[lineB[1]]
                vector_b1 = embedding[entity_b1]
                vector_b2 = embedding[entity_b2]
                vector2 = vector_b2 - vector_b1

                result = self.metric.compute(vector1, vector2)
                is_similar = self.metric.is_better_than_noise(result, embedding)

                yield CaseResult([(entity_a1, entity_a2), (entity_b1, entity_b2)], True, result, is_similar)
