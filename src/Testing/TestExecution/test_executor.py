import logging
import math
import multiprocessing
from queue import Queue
from typing import List

from src.Testing.Result.category_result import CategoryResult
from src.Testing.TaskConfiguration.task_category import TaskCategory
from src.Testing.TestConfiguration.test_configuration import TestConfiguration


class TestExecutor:

    def __init__(self, test_configuration: TestConfiguration, number_of_workers: int = 16):
        self._test_configuration = test_configuration
        self._number_of_workers: int = number_of_workers

    def run(self):
        def _run_categories(categories_: List[TaskCategory], queue_: Queue):
            def _run_category(category_: TaskCategory):
                result = CategoryResult(category_)

                if not category_.enabled:
                    return result

                for count, task in enumerate(category_.tasks):
                    logging.info(
                        f"     {category_.name} :: [{count + 1} / {len(category_.tasks)} ({(count + 1) / len(category_.tasks) * 100} %)] {task.name}")
                    result.add_task_result(task.run(self._test_configuration))

                return result.finalize()

            for index, cat in enumerate(categories_):
                logging.info(
                    f"[{index + 1}/{len(categories_)} ({(index + 1) / len(categories_) * 100} %)] {cat.name}")
                queue_.put(_run_category(cat))

        categories = set(self._test_configuration.categories)
        for category in self._test_configuration.categories:
            for sub_category in category.categories_recursive():
                categories.add(sub_category)

        categories = list(categories)
        queue: Queue = Queue()
        batch_size: int = math.ceil(len(categories) / self._number_of_workers)
        workers: List[multiprocessing.Process] = []
        for i in range(self._number_of_workers):
            batch: List[TaskCategory] = categories[i * batch_size: (i + 1) * batch_size]
            worker = multiprocessing.Process(
                target=_run_categories,
                args=(batch, queue)
            )
            workers.append(worker)
            worker.start()

        for worker in workers:
            worker.join()

        return list(queue.queue)
