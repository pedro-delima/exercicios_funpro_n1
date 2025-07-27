#####################################
# NOME DO SCRIPT: media_funcao.py
# OBJETIVO: Calcular a média de dois números utilizando funções e interface externa
# AUTOR: Allan Kelvin
# DATA CRIAÇÃO: 05.05.25
# EXEMPLO DE USO: python media_funcao.py
# ALTERAÇÕES:
#   DIA X - INCLUÍDA FUNÇÃO ORDENAÇÃO (opcional)
#   DIA Y - CORREÇÃO DE ALGUMA COISA
#####################################

# IMPORTAR AS BIBLIOTECAS
import interface  # módulo externo com msg_inicial()

# DEFINIR FUNÇÕES
def msg_final():
    print("\n=========== FIM DO PROGRAMA ===========")

def entrada_dados():
    x1 = float(input("Entre com o número 1: "))
    x2 = float(input("Entre com o número 2: "))
    return [x1, x2]

def calc_media(n1=0, n2=0):
    m = (n1 + n2) / 2
    return m

def saida(valor):
    print('---------------------------------')
    print(f"O resultado da média é: {valor:.2f}")

# CORPO DO PROGRAMA
interface.msg_inicial("MEDIA")
[num1, num2] = entrada_dados()
media = calc_media(num1, num2)
saida(media)
msg_final()