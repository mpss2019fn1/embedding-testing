from src.Testing.Result.case_result import CaseResult
from src.Testing.Task.abstract_task import AbstractTask


class AnalogyTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "analogy"

    @classmethod
    def task_type(cls):
        from src.Testing.Task.task_type import TaskType
        return TaskType.ANALOGY

    def _run(self):
        embedding = self._test_configuration.embedding
        linking = self._test_configuration.entity_linking
        labels = self._test_configuration.entity_labels
        for indexA, lineA in enumerate(self._test_set_lines()):
            for indexB, lineB in enumerate(self._test_set_lines()):
                if indexA >= indexB:
                    continue

                a = linking[lineA[0]]
                b = linking[lineA[1]]
                c = linking[lineB[0]]
                d = linking[lineB[1]]

                prediction = embedding.word_vectors.most_similar(positive=[a, c], negative=[b], topn=1)[0]

                label_a = labels[lineA[0]]
                label_b = labels[lineA[1]]
                label_c = labels[lineB[0]]
                label_d = labels[lineB[1]]

                yield CaseResult(f"{label_a} : {label_b} like {label_c} : [?]", label_d, prediction[0], prediction[0] == d)
