from reserva import Reserva

class Assento(Reserva):
    def __init__(self, numero, tipo):
        self._numero        = numero
        self._tipo          = tipo
        self._disponivel    = True
        self._cliente       = None

    @property
    def numero(self):
        return self._numero

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        if value not in ["Econômica", "Executiva", "Primeira Classe"]:
            raise ValueError("Tipo de assento inválido")
        self._tipo = value

    @property
    def disponivel(self):
        return self._disponivel

    @property
    def cliente(self):
        return self._cliente

    def reservar(self, cliente):
        if self._disponivel:
            self._cliente = cliente
            self._disponivel = False
            return True
        return False

    