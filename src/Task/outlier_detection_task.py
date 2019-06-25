from src.Task import AbstractTask


class OutlierDetectionTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "outlier_detection"

    @classmethod
    def task_type(cls):
        from src.Task import TaskType
        return TaskType.OUTLIER_DETECTION

    def run(self):
        pass
