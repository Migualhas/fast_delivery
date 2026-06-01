import re

def validar_float(mensagem):
    """Garante que o usuário digite um número decimal válido e positivo (para peso/distância)."""
    while True:
        try:
            valor = float(input(mensagem).strip())
            if valor <= 0:
                print("O valor deve ser maior que zero!")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números (use ponto para decimais).")

def validar_opcao_menu(opcao, opcoes_validas):
    """Valida se a opção digitada está entre as permitidas."""
    return opcao in opcoes_validas

def validar_cpf(mensagem_input):
    """
    Solicita e valida o CPF digitado pelo usuário.
    Retorna apenas os 11 dígitos limpos se for válido.
    """
    while True:
        cpf = input(mensagem_input).strip()
        
        # Remove quaisquer caracteres que não sejam números
        cpf_limpo = re.sub(r'\D', '', cpf)
        
        # Verifica tamanho ou sequências repetidas óbvias
        if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
            print("CPF inválido! O CPF deve conter 11 dígitos válidos. Tente novamente.")
            continue
            
        # --- Cálculo do 1º Dígito Verificador ---
        soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        digito_1 = 0 if resto == 10 else resto
        
        # --- Cálculo do 2º Dígito Verificador ---
        soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        digito_2 = 0 if resto == 10 else resto
        
        # Verifica se os dígitos calculados batem com os digitados
        if int(cpf_limpo[9]) == digito_1 and int(cpf_limpo[10]) == digito_2:
            return cpf_limpo
        else:
            print("CPF inválido! Os dígitos verificadores não batem. Tente novamente.")


def validar_cnh(mensagem_input):
    """
    Solicita e valida a CNH digitada pelo usuário.
    Garante a estrutura essencial de 11 dígitos numéricos reais e não repetidos.
    """
    while True:
        cnh = input(mensagem_input).strip()
        
        # Remove caracteres não numéricos
        cnh_limpa = re.sub(r'\D', '', cnh)
        
        # Uma CNH estruturalmente válida possui exatamente 11 dígitos numéricos e não é repetida
        if len(cnh_limpa) != 11 or cnh_limpa == cnh_limpa[0] * 11:
            print("CNH inválida! O documento deve conter exatamente 11 dígitos numéricos. Tente novamente.")
            continue
            
        return cnh_limpa