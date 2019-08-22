from src.Result.case_result import CaseResult
from src.Task.abstract_task import AbstractTask


class AnalogyTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "analogy"

    @classmethod
    def task_type(cls):
        from src.Task.task_type import TaskType
        return TaskType.ANALOGY

    def _run(self, topn=5):
        embedding = self._test_configuration.embedding
        linking = self._test_configuration.entity_linking
        for indexA, lineA in enumerate(self._test_set_lines()):
            for indexB, lineB in enumerate(self._test_set_lines()):
                if indexA >= indexB:
                    continue

                a = linking[lineA[0]]
                b = linking[lineA[1]]
                c = linking[lineB[0]]
                d = linking[lineB[1]]

                predictions = embedding.word_vectors.most_similar(positive=[a, c], negative=[b], topn=topn)
                top_entities = [entity for entity, _ in predictions]

                yield CaseResult([(a, b), (c, "?")], d, top_entities, d in top_entities)
