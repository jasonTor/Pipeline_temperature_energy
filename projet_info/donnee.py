from abc import ABC, abstractclassmethod, abstractmethod

class Donnee(ABC):

    @abstractmethod
    def importer(self):
        pass