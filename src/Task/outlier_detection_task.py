from src.Task import AbstractTask


class OutlierDetectionTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "outlier_detection"

    def run(self):
        pass
