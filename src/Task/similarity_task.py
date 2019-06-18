from src.Task import AbstractTask


class SimilarityTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "similarity"

    @classmethod
    def task_type(cls):
        from src.Task import TaskType
        return TaskType.SIMILARITY

    def run(self):
        pass
