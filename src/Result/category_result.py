import time

from src.Result.task_result import TaskResult
from src.TaskConfiguration.task_category import TaskCategory


class CategoryResult:

    DISABLED_PREFIX = "#"

    def __init__(self, category: TaskCategory):
        self.category = category
        self.enabled = category.enabled
        self.task_results = []
        self.category_results = []
        self._started = time.time()
        self._ended = None

    def add_task_result(self, task_result: TaskResult):
        self._raise_if_ended()
        self.task_results.append(task_result)

    def add_category_result(self, category_result):
        self._raise_if_ended()
        self.category_results.append(category_result)

    def finalize(self):
        self._raise_if_ended()
        self._ended = time.time()

    def has_results(self):
        self._raise_if_not_ended()
        return self.enabled and (self.category_results or self.task_results)

    def pass_rate(self):
        self._raise_if_not_ended()

        if not self.has_results():
            return 0

        all_case_results = list(self.case_results_recursive())
        number_passed_cases = sum(1 for case_result in all_case_results if case_result.passed)
        pass_rate = number_passed_cases / len(all_case_results)
        pass_rate *= 100.0

        return pass_rate

    def case_results_recursive(self):
        for task_result in self.task_results_recursive():
            yield from task_result.case_results

    def task_results_recursive(self):
        yield from self.task_results

        for category_result in self.category_results:
            yield from category_result.task_results_recursive()

    def execution_duration(self):
        self._raise_if_not_ended()
        if not self.has_results():
            return 0

        return self._ended - self._started

    def _raise_if_ended(self):
        if self._ended:
            raise Exception("This category result has already been finalized")

    def _raise_if_not_ended(self):
        if not self._ended:
            raise Exception("This category result has not yet been finalized")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.print("")

    def print(self, indent):
        self._raise_if_not_ended()

        representation = f"{self.category.name}"

        if not self.enabled:
            return indent + f"{self.DISABLED_PREFIX} {representation}"

        representation = f"{representation} [{'%06.2f' % self.pass_rate()}%] in {'%.3f' % self.execution_duration()}s"
        for task_result in self.task_results:
            printed_task_result = task_result.print(indent + "\t")
            representation = f"{representation}\n{printed_task_result}"

        for category_result in self.category_results:
            printed_category_result = category_result.print(indent + "\t")
            representation = f"{representation}\n{printed_category_result}"

        return indent + representation

