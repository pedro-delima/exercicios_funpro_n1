#####################################
# NOME DO SCRIPT: media.py
# OBJETIVO: Calcular a média de dois números
# AUTOR: Allan Kelvin
# DATA CRIAÇÃO: 05.05.25
# EXEMPLO DE USO: python media.py
# ALTERAÇÕES:
#   - DIA X: INCLUÍDA FUNÇÃO DE ORDENAÇÃO (futura)
#   - DIA Y: CORREÇÃO DE ALGUMA COISA
#####################################

import os

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def exibir_menu():
    """Exibe o cabeçalho do programa."""
    print("========================================")
    print("============ PROGRAMA MÉDIA ============\n")

def ler_dados():
    """Lê os dois números fornecidos pelo usuário."""
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1, n2

def calcular_media(n1, n2):
    """Calcula a média entre dois números."""
    return (n1 + n2) / 2

def exibir_resultado(media):
    """Exibe a média calculada."""
    print("----------------------------------------")
    print(f"A média entre os dois números é: {media:.2f}")

def finalizar():
    """Exibe a mensagem de finalização."""
    print("\n=========== FIM DO PROGRAMA ===========")

# ================================
# PROGRAMA PRINCIPAL
# ================================

def main():
    limpar_tela()
    exibir_menu()
    numero1, numero2 = ler_dados()
    media = calcular_media(numero1, numero2)
    exibir_resultado(media)
    finalizar()

# Executa o programa
if __name__ == "__main__":
    main()