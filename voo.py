from assento import Assento
import random


class Voo:
    
    def __init__  (self,numero, origem, destino, preco, tripulacao, piloto):
        self.numero         = numero
        self.origem         = origem
        self.destino        = destino
        self.assentos       = []
        self.preco          = preco
        self.tripulacao     = tripulacao
        self.piloto         = piloto
        

        tipos = ["Econômica", "Executiva", "Primeira Classe"]
        
        for i in range(250):
            tipo = random.choice(tipos)
            assento = Assento(i + 1, tipo)
            self.assentos.append(assento)
            
              
            
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def origem(self):
        return self._origem
    
    @origem.setter
    def origem(self, value):
        self._origem = value

    @property
    def destino(self):
        return self._destino
    
    
    @destino.setter
    def destino(self, value):
        self._destino = value

    @property
    def preco(self):
        return self._preco
    
    
    @preco.setter
    def preco(self, value):
        self._preco = value

    @property
    def tripulacao(self):
        return self._tripulacao

    @tripulacao.setter
    def tripulacao(self, value):
        self._tripulacao = value

    @property
    def piloto(self):
        return self._piloto
    
    @piloto.setter
    def piloto(self, value):
        self._piloto = value

    @property
    def assentos(self):
        return self._assentos
    
    @assentos.setter    
    def assentos(self, value):      
        self._assentos = value
            
    
    
    def assentos_aleatorios(self):
        print("Mostrando 10 assentos aleatórios:")

        contador = 0

        while contador < 10:
            assento = random.choice(self.assentos)  

            if assento.disponivel:
                status = "Livre"
            else:
                status = f"Ocupado por {assento.cliente.nome}"
            
            print(f"Assento {assento.numero} - {assento.tipo} - {status}")

            contador += 1