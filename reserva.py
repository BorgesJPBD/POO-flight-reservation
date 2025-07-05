from abc import ABC, abstractmethod

class Reserva(ABC):

    @abstractmethod
    def reservar(self, cliente):
        """
        Método para reservar algo
        """
        pass