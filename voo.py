class Voo:
    
    def __init__  (self,numero, origem, destino, assentos, preco):
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.assentos = assentos
        self.preco = preco
        


        print(self.preco)
        
        voo1 = Voo("V001", "SP", "RJ", [], 1500.0)