import logging

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

                a = linking[lineA[0]]
                b = linking[lineA[1]]
                c = linking[lineB[0]]
                d = linking[lineB[1]]

                if a.upper() in embedding.word_vectors.wv:
                    a = a.upper()
                elif a.lower() in embedding.word_vectors.wv:
                    a = a.lower()

                if b.upper() in embedding.word_vectors.wv:
                    b = b.upper()
                elif b.lower() in embedding.word_vectors.wv:
                    b = b.lower()

                if c.upper() in embedding.word_vectors.wv:
                    c = c.upper()
                elif c.lower() in embedding.word_vectors.wv:
                    c = c.lower()

                if d.upper() in embedding.word_vectors.wv:
                    d = d.upper()
                elif d.lower() in embedding.word_vectors.wv:
                    d = d.lower()


                label_a = labels[lineA[0]]
                label_b = labels[lineA[1]]
                label_c = labels[lineB[0]]
                label_d = labels[lineB[1]]

                if any(x not in embedding.word_vectors.wv for x in [a, b, c, d]):
                    logging.warning(f"Any of {[a, b, c, d]} is not in vocabulary")
                    yield CaseResult(f"{label_a} : {label_b} like {label_c} : [?]", label_d, "OUT OF VOCABULARY", False)
                    continue

                predictions = embedding.word_vectors.most_similar(positive=[b, c], negative=[a], topn=topn)
                top_entities = [entity.lower() for entity, _ in predictions]

                top_entity_labels = ', '.join(labels[entity] for entity in top_entities)

                if label_d.lower() in top_entities:
                    yield CaseResult(f"{label_a} : {label_b} like {label_c} : [?]", label_d, top_entity_labels, True)
                else:
                    yield CaseResult(f"{label_a} : {label_b} like {label_c} : [?]", d, top_entity_labels,
                                     d.lower() in top_entities)
