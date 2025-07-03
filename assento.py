class Assento:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponivel = True
        self.cliente = None

    def reservar(self,cliente): #Esse método é chamado quando alguém tenta reservar o assento   #Ele recebe como parâmetro o cliente que vai sentar ali
        if self.disponivel: #Aqui o sistema verifica se o assento está disponível (livre) #Se self.disponivel for True, o assento está vazio e pode ser reservado
            self.cliente = cliente # Associa o cliente ao assento #Se o assento estiver livre, o cliente é atribuído ao assento
            self.disponivel = False #Agora o assento não está mais disponível
            return True #Retorna True para indicar que a reserva foi bem-sucedida
        else: #Se o assento não estiver disponível (self.disponivel for False)
            return False

    