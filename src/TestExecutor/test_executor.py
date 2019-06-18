from src.Task import AbstractTask
from src.TaskConfiguration import TaskCategory
from src.TestConfiguration.test_configuration import TestConfiguration


class TestExecutor:

    def __init__(self, test_configuration: TestConfiguration):
        self._test_configuration = test_configuration

    def run(self):
        for category in self._test_configuration.categories:
            self.run_category(category)

    def run_category(self, category: TaskCategory):
        if not category.enabled:
            return

        for task in category.tasks:
            self.run_task(task)

        for sub_category in category.categories:
            self.run_category(sub_category)

    def run_task(self, task: AbstractTask):
        if not self._test_configuration.is_enabled(task.task_type()):
            return

