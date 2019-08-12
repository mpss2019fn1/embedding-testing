from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

from src.Testing.Embedding.embedding import Embedding
from src.Testing.Result.case_result import CaseResult
from src.Testing.Task.abstract_task import AbstractTask


class AbstractSimilarityTask(AbstractTask, ABC):

    def __init__(self, name, test_set, metric):
        super(AbstractSimilarityTask, self).__init__(name, test_set)
        self.metric = metric
        self._current_group_similarities: List[Tuple[int, float]] = []
        self._current_group_labels: List[Tuple[int, Tuple[str, str]]] = []
        self._current_group_id: Optional[int] = None

    def _run(self):
        embedding = self._test_configuration.embedding
        linking = self._test_configuration.entity_linking
        labels = self._test_configuration.entity_labels
        for line in self._test_set_lines():
            entity1 = linking[line[0]]
            entity2 = linking[line[1]]
            group_id: int = int(line[2])
            rank: int = int(line[3])
            label1: str = labels[entity1]
            label2: str = labels[entity2]
            vector1 = embedding[entity1]
            vector2 = embedding[entity2]

            similarity: float = self.metric.compute(vector1, vector2)

            if self._current_group_id is None:
                self._current_group_id = group_id

            if self._current_group_id == group_id:
                self._current_group_similarities.append((rank, similarity))
                self._current_group_labels.append((rank, (label1, label2)))
                continue

            yield self._perform_similarity_test(embedding)

            self._current_group_similarities = [(rank, similarity)]
            self._current_group_labels = [(rank, (label1, label2))]
            self._current_group_id = group_id

        yield self._perform_similarity_test(embedding)

    def _perform_similarity_test(self, embedding: Embedding):
        self._current_group_similarities.sort(key=lambda item: item[0], reverse=False)
        self._current_group_labels.sort(key=lambda item: item[0], reverse=False)

        test_input: str = " >\n".join([f"[{labels[1][0]}, {labels[1][1]}]" for labels in self._current_group_labels])

        best_similarity: float = self._current_group_similarities[0][1]

        if not self.metric.is_better_than_noise(best_similarity, embedding):
            return CaseResult(test_input, self._stringify_better_than_noise(embedding), best_similarity, False)

        for i in range(1, len(self._current_group_similarities)):
            expected: float = self._current_group_similarities[i][1]
            actual: float = self._current_group_similarities[i-1][1]

            if not self.metric.is_better_than(actual, expected):
                a: str = self._current_group_labels[i - 1][1][0]
                b: str = self._current_group_labels[i - 1][1][1]
                c: str = self._current_group_labels[i][1][0]
                d: str = self._current_group_labels[i][1][1]
                expected_output: str = f"[{a, b}] > [{c, d}]"
                actual_output: str = f"[{a, b}] <= [{c, d}]"
                return CaseResult(test_input, expected_output, actual_output, False)

        return CaseResult(test_input, "similarity hierarchy", True, True)

    @abstractmethod
    def _stringify_better_than_noise(self, embedding: Embedding):
        raise NotImplementedError
