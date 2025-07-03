from assento import Assento
import random


class Voo:
    
    def __init__  (self,numero, origem, destino, preco, tripulacao, piloto):
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.assentos = []
        self.preco = preco
        self.tripulacao = tripulacao
        self.piloto = piloto
        

        tipos = ["Econômica", "Executiva", "Primeira Classe"]
        
        for i in range(250):
            tipo = random.choice(tipos)
            assento = Assento(i + 1, tipo)
            self.assentos.append(assento)
            
    
    
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