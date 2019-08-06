import math
import multiprocessing
from typing import List

from src.Testing.Result.category_result import CategoryResult
from src.Testing.TaskConfiguration.task_category import TaskCategory
from src.Testing.TestConfiguration.test_configuration import TestConfiguration
from src.Testing.TestExecution.category_runner import CategoryRunner


class TestExecutor:

    def __init__(self, test_configuration: TestConfiguration, number_of_workers: int = 16):
        self._test_configuration = test_configuration
        self._number_of_workers: int = number_of_workers

    def run(self):
        categories = set(self._test_configuration.categories)
        for category in self._test_configuration.categories:
            for sub_category in category.categories_recursive():
                categories.add(sub_category)

        categories = list(categories)
        manager: multiprocessing.Manager() = multiprocessing.Manager()
        results: List[CategoryResult] = manager.list()

        batch_size: int = math.ceil(len(categories) / self._number_of_workers)
        workers: List[CategoryRunner] = []
        for i in range(self._number_of_workers):
            batch: List[TaskCategory] = categories[i * batch_size: (i + 1) * batch_size]
            category_runner: CategoryRunner = CategoryRunner(self._test_configuration, batch, results)
            category_runner.start()
            workers.append(category_runner)

        for worker in workers:
            worker.join()

        return list(results)
