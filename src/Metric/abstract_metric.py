from abc import ABC, abstractmethod


class AbstractMetric(ABC):

    @classmethod
    @abstractmethod
    def configuration_identifier(cls):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def task_metric(cls):
        raise NotImplementedError

    @abstractmethod
    def compute(self, vector1, vector2):
        raise NotImplementedError

    @abstractmethod
    def is_better_than_noise(self, result, embedding):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError
