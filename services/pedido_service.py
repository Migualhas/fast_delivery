from modelos.pedido import Pedido

lista_pedido = []

def criar_pedido(codigo, cliente, peso, distancia, tipo_pedido):
    if cliente:
        novo_pedido = Pedido(codigo, cliente, peso, distancia, tipo_pedido)
        lista_pedido.append(novo_pedido)
        return novo_pedido
    else:
        print("Erro: Cliente inválido para vinculação.")
        return None

def buscar(codigo, retornar_objeto=False):
    for pedido in lista_pedido:
        if pedido.codigo == codigo:
            return pedido
    return None

def listar():
    if not lista_pedido:
        print("Nenhum pedido cadastrado.")
        return
    for pedido in lista_pedido:
        print(f"Código: {pedido.codigo} | Cliente: {pedido.cliente.nome} | Tipo: {pedido.tipo_entrega}")