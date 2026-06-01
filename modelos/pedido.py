class Pedido:
    def __init__(self, codigo, cliente, peso, distancia, tipo_entrega):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__tipo_entrega = tipo_entrega

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, novo_peso):
        if novo_peso > 0:
            self.__peso = novo_peso
        else:
            raise ValueError("O peso deve ser maior que zero.")

    @property
    def distancia(self):
        return self.__distancia
    
    @distancia.setter
    def distancia(self, nova_distancia):
        if nova_distancia >= 0:
            self.__distancia = nova_distancia
        else:
            raise ValueError("A distância não pode ser negativa.")

    @property
    def tipo_entrega(self):
        return self.__tipo_entrega
    
    @tipo_entrega.setter
    def tipo_entrega(self, novo_tipo):
        self.__tipo_entrega = novo_tipo