""" Provide base class for extractors to build on"""

from abc import ABC, abstractmethod


class Extractor(ABC):
    """ Base class for all extractors """
    @abstractmethod
    def extract(self):
        """ Main method to perform the extraction of data """
