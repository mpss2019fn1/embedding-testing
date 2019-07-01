import time

from src.Result.case_result import CaseResult
from src.Task.abstract_task import AbstractTask


class TaskResult:

    DISABLED_PREFIX = "#"
    TYPE_PREFIX = ":"

    def __init__(self, task: AbstractTask, enabled: bool):
        self.name = task.name
        self._task_type = task.__class__.configuration_identifier()
        self.enabled = enabled
        self.case_results = []
        self._started = time.time()
        self._ended = None

    def add_case_result(self, case_result: CaseResult):
        self._raise_if_ended()
        self.case_results.append(case_result)

    def finalize(self):
        self._raise_if_ended()
        self._ended = time.time()

    def has_results(self):
        self._raise_if_not_ended()
        return self.enabled and self.case_results

    def pass_rate(self):
        self._raise_if_not_ended()

        if not self.has_results():
            return 0

        number_of_passed_cases = sum(1 for case_result in self.case_results if case_result.passed)
        pass_rate = number_of_passed_cases / len(self.case_results)
        pass_rate *= 100.0
        return pass_rate

    def execution_duration(self):
        self._raise_if_not_ended()

        if not self.has_results():
            return 0

        return self._ended - self._started

    def _raise_if_ended(self):
        if self._ended:
            raise Exception("This task result has already been finalized")

    def _raise_if_not_ended(self):
        if not self._ended:
            raise Exception("This task result has not yet been finalized")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.print("")

    def print(self, indent):
        representation = f"{self.name} {TaskResult.TYPE_PREFIX} {self._task_type}"

        if not self.enabled:
            return indent + f"{self.DISABLED_PREFIX} {representation}"

        representation = f"{representation} [{'%06.2f' % self.pass_rate()}%] in {'%.3f' % self.execution_duration()}s"
        for case_result in self.case_results:
            printed_case_result = case_result.print(indent + "\t")
            representation = f"{representation}\n{printed_case_result}"

        return indent + representation
