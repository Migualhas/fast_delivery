from abc import ABC, abstractmethod

# 1. A INTERFACE (O contrato) [cite: 79]
class CalculoFreteInterface(ABC):
    @abstractmethod
    def calcular_frete(self, pedido):
        pass

# 2. IMPLEMENTAÇÃO: Entrega Comum [cite: 84]
class EntregaComum(CalculoFreteInterface):
    def calcular_frete(self, pedido):
        return pedido.distancia * 1.5  # [cite: 147]

# 3. IMPLEMENTAÇÃO: Entrega Expressa [cite: 85]
class EntregaExpressa(CalculoFreteInterface):
    def calcular_frete(self, pedido):
        return pedido.distancia * 3.0  # [cite: 151]

# 4. IMPLEMENTAÇÃO: Entrega Premium [cite: 86]
class EntregaPremium(CalculoFreteInterface):
    def calcular_frete(self, pedido):
        return (pedido.distancia * 5.0) + 20.0  #