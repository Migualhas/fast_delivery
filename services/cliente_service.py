from modelos.cliente import Cliente
from util import formatador

lista_cliente = []

def criar_cliente(nome, cpf, telefone, endereco):
    novo_cliente = Cliente(nome, cpf, telefone, endereco)
    lista_cliente.append(novo_cliente)
    return novo_cliente

def buscar(cpf, retornar_objeto=False):
    for cliente in lista_cliente:
        if cliente.cpf == cpf:
            if retornar_objeto:
                return cliente
            else:
                print(formatador.formatar_dados_cliente(cliente))
                return cliente
    print(f"Cliente com CPF {cpf} não encontrado!")
    return None

def listar():
    if not lista_cliente:
        print("Nenhum cliente cadastrado no sistema ainda.")
        return
    for cliente in lista_cliente:
        print(formatador.formatar_dados_cliente(cliente))