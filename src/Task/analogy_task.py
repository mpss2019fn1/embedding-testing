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

                a = linking[lineA[0]]
                b = linking[lineA[1]]
                c = linking[lineB[0]]
                d = linking[lineB[1]]

                prediction = embedding.word_vectors.most_similar(positive=[c, a], negative=[b], topn=1)[0]

                yield CaseResult([(a, b), (c, "?")], d, prediction, prediction[0] == d)
