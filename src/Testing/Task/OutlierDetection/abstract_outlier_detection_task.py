from abc import ABC, abstractmethod

from src.Testing.Result.case_result import CaseResult
from src.Testing.Task.abstract_task import AbstractTask


class AbstractOutlierDetectionTask(AbstractTask, ABC):

    def __init__(self, name, test_set, metric):
        super(AbstractOutlierDetectionTask, self).__init__(name, test_set)
        self._current_group = []
        self._current_group_labels = []
        self._current_group_id = None
        self._current_outlier = None
        self._current_outlier_label = None
        self.metric = metric

    def _run(self):
        linking = self._test_configuration.entity_linking
        embedding = self._test_configuration.embedding
        labels = self._test_configuration.entity_labels
        for line in self._test_set_lines():
            entity = linking[line[0]]
            label = labels[line[0]]
            group_id = line[1]
            is_outlier = line[2].lower() == "true"

            if not self._current_group_id:
                self._current_group_id = group_id

            if self._current_group_id == group_id:
                self._current_group.append(entity)
                self._current_group_labels.append(label)
                self._current_outlier = entity if is_outlier else self._current_outlier
                self._current_outlier_label = label if is_outlier else self._current_outlier_label
                continue

            yield self._perform_test(embedding)

            self._current_group = [entity]
            self._current_group_labels = [label]
            self._current_group_id = group_id
            self._current_outlier = entity if is_outlier else self._current_outlier
            self._current_outlier_label = label if is_outlier else self._current_outlier_label

        yield self._perform_test(embedding)

    def _perform_test(self, embedding):
        if len(self._current_group) <= 2:
            return CaseResult(self._current_group_labels, "No expected output", "Too few elements in group", False)

        outlier = self._identify_outlier(embedding)
        outlier_index = self._current_group.index(outlier)
        return CaseResult(self._current_group_labels, self._current_outlier_label,
                          self._current_group_labels[outlier_index], self._current_outlier == outlier)

    @abstractmethod
    def _identify_outlier(self, embedding):
        raise NotImplementedError
