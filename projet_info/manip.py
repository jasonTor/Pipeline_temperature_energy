from abc import ABC, abstractclassmethod, abstractmethod

class Manipulation(ABC):

    @abstractmethod
    def get_indice_var(self, var):
        pass