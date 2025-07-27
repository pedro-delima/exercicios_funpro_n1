import os
import math

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def exibir_menu():
    """Exibe o menu de apresentação."""
    print("===============================================")
    print("========== PROGRAMA CALCULAR ÁREA ============\n")

def ler_raio():
    """Lê o raio digitado pelo usuário e retorna como float."""
    return float(input("Digite o raio do círculo: "))

def calcular_area(raio):
    """Calcula e retorna a área de um círculo dado o raio."""
    return math.pi * raio ** 2

def exibir_resultado(area):
    """Exibe o resultado da área formatado."""
    print("-----------------------------------------------")
    print(f"A área do círculo é: {area:.2f} m²")

def finalizar():
    """Exibe mensagem de finalização."""
    print("\n=========== FIM DO PROGRAMA ===========")

# ==========================
# PROGRAMA PRINCIPAL
# ==========================

def main():
    limpar_tela()
    exibir_menu()
    raio = ler_raio()
    area = calcular_area(raio)
    exibir_resultado(area)
    finalizar()

# Executa o programa
if __name__ == "__main__":
    main()