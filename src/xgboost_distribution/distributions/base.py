"""Distribution base class
"""
from abc import ABC, abstractmethod
from collections import namedtuple


class BaseDistribution(ABC):
    """Base class distribution for XGBDistribution.

    Note that by design all distributions are **stateless**.
    A distribution is thus a collection of functions that operate on the data
    (`y`) and the outputs of the xgboost Booster (`params`).
    """

    def __init__(self):
        self.Predictions = namedtuple("Predictions", (p for p in self.params))

    @property
    @abstractmethod
    def params(self):
        pass

    @abstractmethod
    def starting_params(self, y):
        pass

    @abstractmethod
    def gradient_and_hessian(self, y, params):
        pass

    @abstractmethod
    def loss(self, y, params):
        pass

    @abstractmethod
    def predict(self, params):
        pass