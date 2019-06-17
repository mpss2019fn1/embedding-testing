from src.Task import AbstractTask


class AnalogyTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "analogy"

    def run(self):
        pass
