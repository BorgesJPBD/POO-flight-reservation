
class Cliente:

    def __init__(self, nome, cpf, telefone, endereco):
        self.nome       = nome
        self.cpf        = cpf
        self.telefone   = telefone
        self.endereco   = endereco
          
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Nome inválido")
        self._nome = value.strip()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("CPF inválido")
        self._cpf = value.strip()

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Telefone inválido")
        self._telefone = value.strip()

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Endereço inválido")
        self._endereco = value.strip()