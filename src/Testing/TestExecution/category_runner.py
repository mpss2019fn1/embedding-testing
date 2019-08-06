import logging
from multiprocessing import Process
from typing import List

from src.Testing.Result.category_result import CategoryResult
from src.Testing.Task.abstract_task import AbstractTask
from src.Testing.TaskConfiguration.task_category import TaskCategory
from src.Testing.TestConfiguration.test_configuration import TestConfiguration


class CategoryRunner(Process):

    def __init__(self,
                 test_configuration: TestConfiguration,
                 categories: List[TaskCategory],
                 results: List[CategoryResult]):
        super(CategoryRunner, self).__init__()
        self._test_configuration: TestConfiguration = test_configuration
        self._categories: List[TaskCategory] = categories
        self._results: List[CategoryResult] = results

    def run(self) -> None:
        for index, category in enumerate(self._categories):
            logging.info(
                f"[{index + 1}/{len(self._categories)} ({(index + 1) / len(self._categories) * 100} %)] {category.name}")
            self._results.append(self._run_category(category))

    def _run_category(self, category: TaskCategory):
        result = CategoryResult(category)

        if not category.enabled:
            return result

        for task in category.tasks:
            result.add_task_result(self._run_task(task))

        return result.finalize()

    def _run_task(self, task: AbstractTask):
        return task.run(self._test_configuration)
