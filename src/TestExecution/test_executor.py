from src.Result.category_result import CategoryResult
from src.Task.abstract_task import AbstractTask
from src.TaskConfiguration.task_category import TaskCategory
from src.TestConfiguration.test_configuration import TestConfiguration


class TestExecutor:

    def __init__(self, test_configuration: TestConfiguration):
        self._test_configuration = test_configuration

    def run(self):
        for category in self._test_configuration.categories:
            yield self.run_category(category)

    def run_category(self, category: TaskCategory):
        result = CategoryResult(category)

        if not category.enabled:
            return result

        for task in category.tasks:
            result.add_task_result(self.run_task(task))

        for sub_category in category.categories:
            result.add_category_result(self.run_category(sub_category))

        return result.finalize()

    def run_task(self, task: AbstractTask):
        return task.run(self._test_configuration)
