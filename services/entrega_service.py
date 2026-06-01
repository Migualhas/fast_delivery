from modelos.entrega import Entrega
from modelos.entregador import Entregador
from interfaces.calculo_frete_interface import EntregaComum, EntregaExpressa, EntregaPremium

lista_entrega = []
lista_entregadores = []

def criar_entrega(status, pedido):
    if not pedido:
        return None
        
    # Polimorfismo em ação [cite: 87, 91]
    if pedido.tipo_entrega.lower() == "comum":
        calculador = EntregaComum()
    elif pedido.tipo_entrega.lower() == "expressa":
        calculador = EntregaExpressa()
    else:
        calculador = EntregaPremium()
        
    frete = calculador.calcular_frete(pedido)
    nova_entrega = Entrega(status, pedido, frete)
    lista_entrega.append(nova_entrega)
    print("\n✅ Entrega vinculada e frete calculado com sucesso!")
    return nova_entrega

def buscar(codigo):
    for entrega in lista_entrega:
        if entrega.pedido.codigo == codigo:
            exibir_resumo_entrega(entrega)
            return entrega
    print(f"Entrega do pedido {codigo} não encontrada!")
    return None

def listar():
    if not lista_entrega:
        print("Nenhum pedido/entrega no sistema até o momento.")
        return
    for entrega in lista_entrega:
        exibir_resumo_entrega(entrega)

def atualizar_status(novo_status, codigo):
    for entrega in lista_entrega:
        if entrega.pedido.codigo == codigo:
            entrega.status = novo_status
            print(f"Status atualizado para: {novo_status}")
            return
    print(f"Pedido {codigo} não encontrado!")

def exibir_resumo_entrega(entrega):
    print(
        f"========== RESUMO DA ENTREGA ==========\n"
        f"Código:       {entrega.pedido.codigo}\n"
        f"Cliente:      {entrega.pedido.cliente.nome}\n"
        f"Status:       {entrega.status}\n"
        f"Frete:        R$ {entrega.frete:.2f}\n"
        f"======================================="
    )

def cadastrar_entregador(nome, veiculo, cnh):
    if not nome or not veiculo or not cnh:
        print("\n Erro: Todos os campos são obrigatórios!")
        return None
    novo = Entregador(nome, veiculo, cnh)
    lista_entregadores.append(novo)
    print(f"\nEntregador {nome} cadastrado com sucesso!")
    return novo

def listar_entregadores():
    if not lista_entregadores:
        print("\nNenhum entregador cadastrado.")
        return
    for ent in lista_entregadores:
        print(f"\nNome: {ent.nome} | Veículo: {ent.veiculo} | CNH: {ent.cnh}")