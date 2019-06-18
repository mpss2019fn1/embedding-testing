from src.Task import AbstractTask


class NeighborhoodTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "neighborhood"

    @classmethod
    def task_type(cls):
        from src.Task import TaskType
        return TaskType.NEIGHBORHOOD

    def run(self):
        pass
