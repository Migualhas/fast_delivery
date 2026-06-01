from modelos.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        super().__init__(nome)
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        if len(str(novo_telefone)) >= 8:
            self.__telefone = novo_telefone
        else:
            raise ValueError("Telefone deve conter pelo menos 8 dígitos.")

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco