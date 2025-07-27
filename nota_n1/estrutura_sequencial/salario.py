#####################################
# NOME DO SCRIPT: salario.py
# OBJETIVO: Calcular o salário mensal com base no valor por hora e horas trabalhadas
# AUTOR: Allan Kelvin
# DATA CRIAÇÃO: 14.05.25
# EXEMPLO DE USO: python salario.py
#####################################

import os

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def exibir_menu():
    """Exibe o cabeçalho do programa."""
    print("===============================================")
    print("========== PROGRAMA CALCULAR SALÁRIO ==========\n")

def ler_dados():
    """Lê os dados de entrada: salário por hora e horas trabalhadas."""
    ganho_hora = float(input("Digite o salário por hora: R$ "))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
    return ganho_hora, horas_trabalhadas

def calcular_salario(ganho_hora, horas_trabalhadas):
    """Calcula o salário total."""
    return ganho_hora * horas_trabalhadas

def exibir_resultado(salario):
    """Exibe o resultado final."""
    print("-----------------------------------------------")
    print(f"Salário total do mês: R$ {salario:.2f}")

def finalizar():
    """Exibe a mensagem de encerramento."""
    print("\n=========== FIM DO PROGRAMA ===========")

# ================================
# PROGRAMA PRINCIPAL
# ================================

def main():
    limpar_tela()
    exibir_menu()
    ganho_hora, horas_trabalhadas = ler_dados()
    salario_total = calcular_salario(ganho_hora, horas_trabalhadas)
    exibir_resultado(salario_total)
    finalizar()

# Executa o programa
if __name__ == "__main__":
    main()