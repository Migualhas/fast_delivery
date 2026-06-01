import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho(titulo):
    print("=" * 50)
    print(f"{titulo.center(50)}")
    print("=" * 50)
    
def formatar_dados_cliente(cliente):
    return (
        f"--- DADOS DO CLIENTE ---\n"
        f"Nome:     {cliente.nome}\n"
        f"CPF:      {cliente.cpf}\n"
        f"Telefone: {cliente.telefone}\n"
        f"Endereço: {cliente.endereco}\n"
        f"------------------------"
    )