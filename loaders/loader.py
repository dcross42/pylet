""" Provide base class for all loaders to build on """

from abc import ABC, abstractmethod


class Loader(ABC):
    """ Base class for all loaders """

    @abstractmethod
    def load(self):
        """ Main method that executes loading of data """

