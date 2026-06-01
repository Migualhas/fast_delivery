#class Pessoa

class Pessoa:
    def __init__(self,nome,idade=0):
        self.__nome = nome
        self.__idade = idade
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade