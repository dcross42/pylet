""" Provide base class for transformers to build on"""
from abc import ABC, abstractmethod


class Transformer(ABC):
    """ Base class for all transformers """
    @abstractmethod
    def transform(self):
        """ Main method that performs the transformations """
