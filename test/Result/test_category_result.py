from pathlib import Path

import pytest

from src.Result.case_result import CaseResult
from src.Result.category_result import CategoryResult
from src.Result.task_result import TaskResult
from src.Task.Similarity.cosine_similarity_task import CosineSimilarityTask
from src.TaskConfiguration.task_category import TaskCategory


class TestCategoryResult:

    @staticmethod
    def _create_enabled_category_result():
        category = TaskCategory("CategoryName", True, [], [])
        category_result = CategoryResult(category)
        category_result.add_task_result(TestCategoryResult._create_enabled_task_result())

        return category_result

    @staticmethod
    def _create_enabled_task_result(passed=True):
        task = CosineSimilarityTask("CosineSimilarityTask", Path())
        task_result = TaskResult(task, True)
        task_result.add_case_result(CaseResult("expected", "expected", "expected", passed))
        task_result.finalize()

        return task_result

    def test_has_results(self):
        result = self._create_enabled_category_result()
        assert result.has_results()

        result.finalize()
        assert result.has_results()

    def test_has_execution_duration(self):
        result = self._create_enabled_category_result()
        assert result.execution_duration() == 0

        result.finalize()
        assert result.execution_duration() > 0

    def test_pass_rate(self):
        result = self._create_enabled_category_result()
        assert result.pass_rate() == 0

        result.add_task_result(self._create_enabled_task_result(False))
        assert result.pass_rate() == 0

        result.finalize()
        assert result.pass_rate() == 50

    def test_representation_contains_all_case_result(self):
        result = self._create_enabled_category_result()
        result.finalize()

        assert len(str(result).split("\n")) == 3
        assert result.__str__() == result.__repr__()

    def test_representation_contains_all_sub_categories(self):
        result = self._create_enabled_category_result()
        sub_result = self._create_enabled_category_result()
        sub_result.finalize()
        result.add_category_result(sub_result)
        result.finalize()

        assert len(str(result).split("\n")) == 6
        assert result.__str__() == result.__repr__()

    def test_disabled_representation_starts_with_prefix(self):
        category = TaskCategory("CategoryName", False, [], [])
        result = CategoryResult(category)

        assert not result.enabled
        assert str(result).startswith(CategoryResult.DISABLED_PREFIX)
        assert len(str(result).split("\n")) == 1

    def test_empty_result(self):
        category = TaskCategory("CategoryName", True, [], [])
        result = CategoryResult(category)
        result.finalize()

        assert not result.has_results()
        assert result.pass_rate() == 0
        assert result.execution_duration() == 0
        assert len(str(result)) > 0
        assert len(str(result).split("\n")) == 1

    def test_task_results_recursive(self):
        result = self._create_enabled_category_result()
        category_result = self._create_enabled_category_result()
        category_result.finalize()
        result.add_category_result(category_result)
        result.finalize()

        assert len(result.task_results) == 1
        assert len(list(result.task_results_recursive())) == 2

    def test_case_results_recursive(self):
        result = self._create_enabled_category_result()
        category_result = self._create_enabled_category_result()
        category_result.finalize()
        result.add_category_result(category_result)
        result.finalize()

        assert len(result.task_results) == 1
        assert len(result.task_results[0].case_results) == 1
        assert len(result.category_results) == 1
        assert len(list(result.case_results_recursive())) == 2

    def test_add_task_result_raises_if_finalized(self):
        result = self._create_enabled_category_result()
        result.finalize()

        task = CosineSimilarityTask("CosineSimilarityTask", Path())
        task_result = TaskResult(task, True)

        with pytest.raises(Exception):
            result.add_task_result(task_result)

    def test_add_category_result_raises_if_finalized(self):
        result = self._create_enabled_category_result()
        result.finalize()

        category_result = self._create_enabled_category_result()

        with pytest.raises(Exception):
            result.add_category_result(category_result)

    def test_finalize_raises_if_finalized(self):
        result = self._create_enabled_category_result()
        result.finalize()

        with pytest.raises(Exception):
            result.finalize()

    def test_finalize_returns_self(self):
        result = self._create_enabled_category_result()

        assert result == result.finalize()
