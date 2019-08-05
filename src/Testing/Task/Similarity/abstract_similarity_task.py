from abc import ABC, abstractmethod

from src.Testing.Result.case_result import CaseResult
from src.Testing.Task.abstract_task import AbstractTask


class AbstractSimilarityTask(AbstractTask, ABC):

    def __init__(self, name, test_set, metric):
        super(AbstractSimilarityTask, self).__init__(name, test_set)
        self.metric = metric

    def _run(self):
        embedding = self._test_configuration.embedding
        linking = self._test_configuration.entity_linking
        labels = self._test_configuration.entity_labels
        for line in self._test_set_lines():
            entity1 = linking[line[0]]
            entity2 = linking[line[1]]
            vector1 = embedding[entity1]
            vector2 = embedding[entity2]
            is_expected_similar = line[2].lower() == "true"

            result = self.metric.compute(vector1, vector2)
            is_similar = self.metric.is_better_than_noise(result, embedding)

            expected_result = self._stringify_expected_result(is_expected_similar)

            label_a = labels[line[0]]
            label_b = labels[line[1]]

            yield CaseResult([label_a, label_b], expected_result, '%06.4f' % result, is_similar == is_expected_similar)

    @abstractmethod
    def _stringify_expected_result(self, is_expected_similar):
        raise NotImplementedError
