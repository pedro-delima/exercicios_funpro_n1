# Programa para verificar se um ano é bissexto

# Solicita o ano
ano = int(input("Digite um ano: "))

# Verifica se é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")