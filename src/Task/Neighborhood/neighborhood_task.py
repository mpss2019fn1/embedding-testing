from src.Task.abstract_task import AbstractTask


class NeighborhoodTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "neighborhood"

    @classmethod
    def task_type(cls):
        from src.Task.task_type import TaskType
        return TaskType.NEIGHBORHOOD

    def _run(self):
        pass
