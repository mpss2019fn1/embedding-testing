from abc import ABC, abstractmethod


class AbstractMetric(ABC):

    @abstractmethod
    def compute(self, vector1, vector2):
        raise NotImplementedError

    @abstractmethod
    def is_better_than_noise(self, result, embedding):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError
