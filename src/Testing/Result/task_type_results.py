from typing import Dict, List

from src.Testing.Result.case_result import CaseResult
from src.Testing.Task.task_type import TaskType


class TaskTypeResults:

    def __init__(self, category_result):
        self._category_result = category_result
        self._results_by_task_type = self._collect_metrics()

    def _collect_metrics(self) -> Dict[str, float]:
        grouped_case_results: Dict[str, List[CaseResult]] = {}
        for task_type in TaskType:
            grouped_case_results[task_type.value.configuration_identifier()] = []
        for task_result in self._category_result.task_results_recursive():
            grouped_case_results[task_result.task_type].extend(task_result.case_results)

        results: Dict[str, float] = dict.fromkeys([task_type.value.configuration_identifier() for task_type in TaskType], 0)
        for task_type in grouped_case_results:
            number_of_case_results: int = len(grouped_case_results[task_type])
            if number_of_case_results < 1:
                del results[task_type]
                continue
            results[task_type] = sum(1 if case_result.passed else 0 for case_result in grouped_case_results[task_type])
            results[task_type] = results[task_type] / len(grouped_case_results[task_type]) * 100
        return results

    def get_success_rates(self) -> Dict[str, float]:
        return self._results_by_task_type

    def get_success_rate(self, task_type: TaskType) -> float:
        return self._results_by_task_type[task_type.value.configuration_identifier()]
