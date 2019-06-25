import csv
from abc import ABC, abstractmethod


class AbstractTask(ABC):

    @classmethod
    @abstractmethod
    def configuration_identifier(cls):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def task_type(cls):
        raise NotImplementedError

    def __init__(self, name, test_set, metric):
        self.name = name
        self.test_set = test_set
        self.metric = metric
        self._test_configuration = None

    def run(self, test_configuration):
        from src.Result.task_result import TaskResult
        self._test_configuration = test_configuration
        is_enabled = self._test_configuration.is_enabled(self.__class__.task_type())
        task_result = TaskResult(self, is_enabled)
        if not is_enabled:
            return task_result.finalize()

        for case_result in self._run():
            task_result.add_case_result(case_result)

        return task_result.finalize()

    @abstractmethod
    def _run(self):
        raise NotImplementedError

    def _test_set_lines(self):
        with self.test_set.open("r") as test_case_stream:
            csv_reader = csv.reader(test_case_stream, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                yield row
