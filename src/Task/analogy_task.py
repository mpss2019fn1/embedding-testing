from src.Task import AbstractTask


class AnalogyTask(AbstractTask):

    def _run(self):
        pass

    @classmethod
    def configuration_identifier(cls):
        return "analogy"

    @classmethod
    def task_type(cls):
        from src.Task import TaskType
        return TaskType.ANALOGY

    def run(self):
        pass
