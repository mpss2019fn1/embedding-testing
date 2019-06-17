from src.Task import AbstractTask


class NeighborhoodTask(AbstractTask):

    @classmethod
    def configuration_identifier(cls):
        return "neighborhood"

    def run(self):
        pass
