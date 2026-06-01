# =====================================================================
# Ponto de Entrada Principal (Entry Point) - fast_delivery/main.py
# =====================================================================
import sys
import os

# Garante que o Python reconheça as pastas internas do projeto como pacotes válidos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from util.menu import mostrar_menu_principal

def main():
    try:
        # Inicializa o loop do menu principal do sistema via terminal
        mostrar_menu_principal()
    except KeyboardInterrupt:
        # Trata o encerramento forçado amigavelmente (ex: Ctrl + C)
        print("\n\nExecução interrompida pelo usuário. Encerrando o FastDelivery Express...")
        sys.exit(0)

if __name__ == "__main__":
    main()