from modelos.pessoa import Pessoa

class Entregador(Pessoa):
    def __init__(self, nome, veiculo, cnh):
        super().__init__(nome)
        self.__veiculo = veiculo
        self.__cnh = cnh    
        
    @property
    def cnh(self):
        return self.__cnh

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, novo_veiculo):
        self.__veiculo = novo_veiculo