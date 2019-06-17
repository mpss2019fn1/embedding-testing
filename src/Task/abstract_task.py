from abc import ABC, abstractmethod


class AbstractTask(ABC):

    @classmethod
    def configuration_identifier(cls):
        raise NotImplementedError

    def __init__(self, name, test_set, metric):
        self.name = name
        self.test_set = test_set
        self.metric = metric

    @abstractmethod
    def run(self):
        raise NotImplementedError
