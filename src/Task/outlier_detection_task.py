from src.Task.abstract_task import AbstractTask


class OutlierDetectionTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "outlier_detection"

    @classmethod
    def task_type(cls):
        from src.Task.task_type import TaskType
        return TaskType.OUTLIER_DETECTION

    def _run(self):
        pass
