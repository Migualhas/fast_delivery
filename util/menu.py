from services import cliente_service
from services import pedido_service
from services import entrega_service
from util import validador
from util import formatador

def mostrar_menu_principal():
    while True:
        formatador.limpar_tela()
        formatador.exibir_cabecalho("FASTDELIVERY EXPRESS - MENU PRINCIPAL")
        print("[1] Módulo de Clientes")
        print("[2] Módulo de Pedidos")
        print("[3] Módulo de Entregadores")
        print("[0] Sair do Sistema")
        print("-" * 50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_pedidos()
        elif opcao == "3":
            menu_entregadores()
        elif opcao == "0":
            formatador.limpar_tela()
            print("\nSistema FastDelivery encerrado com sucesso.\n")
            break
        else:
            input("\nOpção inválida! Pressione Enter...")

def menu_clientes():
    while True:
        formatador.limpar_tela()
        formatador.exibir_cabecalho("GERENCIAMENTO DE CLIENTES")
        print("[1] Cadastrar Cliente")
        print("[2] Listar Clientes")
        print("[3] Buscar Cliente")
        print("[0] Voltar ao Menu Principal")
        print("-" * 50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            formatador.limpar_tela()
            formatador.exibir_cabecalho("CADASTRO DE CLIENTE")
            nome = input("Nome do Cliente: ").strip()
            cpf = validador.validar_cpf("CPF (apenas números): ")
            telefone = input("Telefone: ").strip()
            endereco = input("Endereço: ").strip()
            
            cliente_service.criar_cliente(nome, cpf, telefone, endereco)
            input("\nPressione Enter para continuar...")
            
        elif opcao == "2":
            formatador.limpar_tela()
            formatador.exibir_cabecalho("LISTAGEM DE CLIENTES")
            cliente_service.listar()
            input("\nPressione Enter para voltar...")
            
        elif opcao == "3":
            formatador.limpar_tela()
            formatador.exibir_cabecalho("BUSCAR CLIENTE")
            cpf = input("Digite o CPF do cliente: ").strip()
            cliente_service.buscar(cpf, False)
            input("\nPressione Enter para voltar...")
            
        elif opcao == "0":
            break

def menu_pedidos():
    while True:
        formatador.limpar_tela()
        formatador.exibir_cabecalho("GERENCIAMENTO DE PEDIDOS")
        print("[1] Criar Pedido")
        print("[2] Listar Pedidos (Histórico)")
        print("[3] Atualizar Status da Entrega")
        print("[0] Voltar ao Menu Principal")
        print("-" * 50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            formatador.limpar_tela()
            formatador.exibir_cabecalho("CRIAR NOVO PEDIDO")
            cpf_cliente = input("Digite o CPF do cliente para o pedido: ").strip()
            cliente = cliente_service.buscar(cpf_cliente, True)
            
            if cliente:
                print(f"Cliente Vinculado: {cliente.nome}")
                print("-" * 50)
                codigo = input("Código do Pedido: ").strip()
                peso = validador.validar_float("Peso da Carga (kg): ") 
                distancia = validador.validar_float("Distância do Trajeto (km): ")
                
                print("\nTipos de Entrega:")
                print("[1] Entrega Comum")
                print("[2] Entrega Expressa")
                print("[3] Entrega Premium")
                tipo_op = input("Selecione o tipo de entrega (1-3): ").strip()
                
                mapa_tipos = {"1": "comum", "2": "expressa", "3": "premium"}
                tipo_entrega = mapa_tipos.get(tipo_op, "comum")
                
                pedido_criado = pedido_service.criar_pedido(codigo, cliente, peso, distancia, tipo_entrega)
                entrega_service.criar_entrega("Em preparação", pedido_criado)
            else:
                print("\n❌ Não é possível criar o pedido. Cliente não cadastrado!")
                
            input("\nPressione Enter para continuar...")
            
        elif opcao == "2":
            formatador.limpar_tela()
            formatador.exibir_cabecalho("HISTÓRICO DE ENTREGAS")
            entrega_service.listar()
            input("\nPressione Enter para voltar...")
            
        elif opcao == "3":
            formatador.limpar_tela()
            formatador.exibir_cabecalho("ATUALIZAR STATUS DA ENTREGA")
            codigo = input("Digite o código do pedido: ").strip()
            entrega = entrega_service.buscar(codigo)
            if entrega:
                print("\nNovos Status Disponíveis:")
                print("[1] Em preparação")
                print("[2] Saiu para entrega")
                print("[3] Entregue")
                print("[4] Cancelado")
                status_op = input("Selecione a nova situação (1-4): ").strip()
                
                mapa_status = {"1": "Em preparação", "2": "Saiu para entrega", "3": "Entregue", "4": "Cancelado"}
                novo_status = mapa_status.get(status_op)
                
                if novo_status:
                    entrega_service.atualizar_status(novo_status, codigo)
                else:
                    print("\n❌ Opção de status inválida.")
            input("\nPressione Enter para voltar...")
            
        elif opcao == "0":
            break

def menu_entregadores():
    while True:
        formatador.limpar_tela()
        formatador.exibir_cabecalho("GERENCIAMENTO DE ENTREGADORES")
        print("[1] Cadastrar Entregador")
        print("[2] Listar Entregadores")
        print("[0] Voltar ao Menu Principal")
        print("-" * 50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            formatador.limpar_tela()
            formatador.exibir_cabecalho("CADASTRO DE ENTREGADOR")
            nome = input("Nome do Entregador: ").strip()
            veiculo = input("Veículo: ").strip()
            cnh = validador.validar_cnh("Carteira de Habilitação (CNH): ")
            entrega_service.cadastrar_entregador(nome, veiculo, cnh)
            input("\nPressione Enter para continuar...")
        elif opcao == "2":
            formatador.limpar_tela()
            formatador.exibir_cabecalho("LISTA DE ENTREGADORES")
            entrega_service.listar_entregadores()
            input("\nPressione Enter para continuar...")
        elif opcao == "0":
            break