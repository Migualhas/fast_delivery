class Entrega:
    def __init__(self, status, pedido, frete):
        self.__status = status
        self.__pedido = pedido
        self.__frete = frete
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        status_permitidos = ["Em preparação", "Saiu para entrega", "Entregue", "Cancelado"] # [cite: 139-142]
        if novo_status in status_permitidos:
            self.__status = novo_status
        else:
            raise ValueError("Status de entrega inválido.")

    @property
    def pedido(self):
        return self.__pedido
    
    @property
    def frete(self):
        return self.__frete

    @frete.setter
    def frete(self, novo_frete):
        if novo_frete >= 0:
            self.__frete = novo_frete
        else:
            raise ValueError("O frete não pode ser negativo.")