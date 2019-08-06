import logging

from src.Testing.Result.category_result import CategoryResult
from src.Testing.Task.abstract_task import AbstractTask
from src.Testing.TaskConfiguration.task_category import TaskCategory
from src.Testing.TestConfiguration.test_configuration import TestConfiguration


class TestExecutor:

    def __init__(self, test_configuration: TestConfiguration):
        self._test_configuration = test_configuration

    def run(self):
        for index, category in enumerate(self._test_configuration.categories):
            logging.info(
                f"{category.name} [{index + 1}/{len(self._test_configuration.categories)} ({(index + 1) / len(self._test_configuration.categories) * 100} %)]")
            yield self._run_category(category, category.name)

    def _run_category(self, category: TaskCategory, indent: str):
        result = CategoryResult(category)

        if not category.enabled:
            return result

        for index, task in enumerate(category.tasks):
            logging.info(
                f"{indent} -> {task.name} [{index + 1} / {len(category.tasks)} ({(index + 1) / len(category.tasks) * 100} %)]")
            result.add_task_result(self.run_task(task))

        for index, sub_category in enumerate(category.categories):
            sub_indent = f"{indent} :: {sub_category.name}"
            logging.info(
                f"{sub_indent} [{index + 1} / {len(category.categories)} ({(index + 1) / len(category.categories) * 100} %)]")
            result.add_category_result(self._run_category(sub_category, sub_indent))

        return result.finalize()

    def run_task(self, task: AbstractTask):
        return task.run(self._test_configuration)
