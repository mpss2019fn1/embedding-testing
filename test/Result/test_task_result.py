from pathlib import Path

import pytest

from src.Result.case_result import CaseResult
from src.Result.task_result import TaskResult
from src.Task.Similarity.cosine_similarity_task import CosineSimilarityTask


class TestTaskResult:

    @staticmethod
    def _create_enabled_task_result():
        task = CosineSimilarityTask("SimilarityTask", Path())
        task_result = TaskResult(task, True)

        case_result = CaseResult("Berlin", "Paris", "Paris", True)
        task_result.add_case_result(case_result)

        return task_result

    def test_has_results(self):
        task_result = TestTaskResult._create_enabled_task_result()
        assert task_result.has_results()

        task_result.finalize()
        assert task_result.has_results()

    def test_has_execution_duration(self):
        task_result = TestTaskResult._create_enabled_task_result()
        assert task_result.execution_duration() == 0

        task_result.finalize()
        assert task_result.execution_duration() > 0

    def test_pass_rate(self):
        task_result = TestTaskResult._create_enabled_task_result()
        assert task_result.pass_rate() == 0

        case_result = CaseResult("Vienna", "London", "Paris", False)
        task_result.add_case_result(case_result)
        assert task_result.pass_rate() == 0

        task_result.finalize()
        assert task_result.pass_rate() == 50

    def test_representation_contains_all_case_results(self):
        task_result = TestTaskResult._create_enabled_task_result()
        case_result = CaseResult("Vienna", "London", "Paris", False)
        task_result.add_case_result(case_result)
        task_result.finalize()

        assert len(str(task_result).split("\n")) == 3
        assert task_result.__str__() == task_result.__repr__()

    def test_disabled_representation_starts_with_prefix(self):
        task = CosineSimilarityTask("SimilarityTask", Path())
        task_result = TaskResult(task, False)

        assert str(task_result).startswith(TaskResult.DISABLED_PREFIX)
        assert len(str(task_result).split("\n")) == 1

    def test_empty_result(self):
        task = CosineSimilarityTask("SimilarityTask", Path())
        task_result = TaskResult(task, True)
        task_result.finalize()

        assert not task_result.has_results()
        assert task_result.pass_rate() == 0.0
        assert task_result.execution_duration() == 0
        assert len(str(task_result)) > 0
        assert len(str(task_result).split("\n")) == 1

    def test_add_case_result_raises_if_finalized(self):
        task = CosineSimilarityTask("SimilarityTask", Path())
        task_result = TaskResult(task, True)
        task_result.finalize()

        with pytest.raises(Exception):
            task_result.add_case_result(CaseResult("input", "expected", "actual", False))

    def test_finalize_raises_if_finalized(self):
        task = CosineSimilarityTask("SimilarityTask", Path())
        task_result = TaskResult(task, True)
        task_result.finalize()

        with pytest.raises(Exception):
            task_result.finalize()

    def test_finalize_returns_self(self):
        task_result = self._create_enabled_task_result()

        assert task_result == task_result.finalize()