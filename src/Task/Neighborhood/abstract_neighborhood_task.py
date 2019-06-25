from abc import ABC

from src.Result.case_result import CaseResult
from src.Task.abstract_task import AbstractTask


class AbstractNeighborhoodTask(AbstractTask, ABC):

    def __init__(self, name, test_set, metric):
        super(AbstractNeighborhoodTask, self).__init__(name, test_set)
        self.metric = metric
        self._current_group = []
        self._current_group_id = None
        self._current_is_expected_similar = None

    def _run(self):
        linking = self._test_configuration.entity_linking
        embedding = self._test_configuration.embedding

        for line in self._test_set_lines():
            entity = linking[line[0]]
            group_id = line[1]
            is_expected_similar = line[2].lower() == "true"

            if not self._current_group_id:
                self._current_group_id = group_id
                self._current_is_expected_similar = is_expected_similar

            if self._current_group_id == group_id:
                self._current_group.append(entity)
                continue

            yield self._test_neighborhood(embedding)

            self._current_group = [entity]
            self._current_group_id = group_id
            self._current_is_expected_similar = is_expected_similar

        yield self._test_neighborhood(embedding)

    def _test_neighborhood(self, embedding):
        result = self.metric.batch_compute([embedding[word] for word in self._current_group])
        is_similar = self.metric.is_better_than_noise(result, embedding)
        passed = is_similar == self._current_is_expected_similar

        return CaseResult(self._current_group, self._current_is_expected_similar, is_similar, passed)
