from src.Task import AbstractTask


class SimilarityTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "similarity"

    def run(self):
        pass
