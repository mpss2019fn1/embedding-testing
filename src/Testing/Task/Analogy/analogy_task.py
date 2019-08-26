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

    def _run(self, topn=5):
        embedding = self._test_configuration.embedding
        linking = self._test_configuration.entity_linking
        labels = self._test_configuration.entity_labels
        for indexA, lineA in enumerate(self._test_set_lines()):
            for indexB, lineB in enumerate(self._test_set_lines()):
                if indexA >= indexB:
                    continue

                a = labels[lineA[0]].upper()   # ! Heuristic to to use unified english label
                b = labels[lineA[1]].upper()   # ! Heuristic to to use unified english label
                c = labels[lineB[0]].upper()   # ! Heuristic to to use unified english label
                d = labels[lineB[1]].upper()   # ! Heuristic to to use unified english label

                if a not in embedding.word_vectors.wv:
                    a = a.lower()
                if b not in embedding.word_vectors.wv:
                    b = b.lower()
                if c not in embedding.word_vectors.wv:
                    c = c.lower()
                if d not in embedding.word_vectors.wv:
                    d = d.lower()

                if any(x not in embedding.word_vectors.wv for x in [a, b, c, d]):
                    continue

                predictions = embedding.word_vectors.most_similar(positive=[b, c], negative=[a], topn=topn)
                top_entities = [entity.lower() for entity, _ in predictions]

                label_a = labels[lineA[0]]
                label_b = labels[lineA[1]]
                label_c = labels[lineB[0]]
                label_d = labels[lineB[1]]

                top_entity_labels = ', '.join(labels[entity] for entity in top_entities)

                if label_d.lower() in top_entities:
                    yield CaseResult(f"{label_a} : {label_b} like {label_c} : [?]", label_d, top_entity_labels, True)
                else:
                    yield CaseResult(f"{label_a} : {label_b} like {label_c} : [?]", d, top_entity_labels,
                                     d.lower() in top_entities)
