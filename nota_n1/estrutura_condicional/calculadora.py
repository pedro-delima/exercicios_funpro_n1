# Programa que realiza operação entre dois números e analisa o resultado

# Leitura dos dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolha da operação
print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = input("Digite o número da operação desejada: ")

# Realiza a operação
if opcao == "1":
    resultado = num1 + num2
    operacao = "+"
elif opcao == "2":
    resultado = num1 - num2
    operacao = "-"
elif opcao == "3":
    resultado = num1 * num2
    operacao = "*"
elif opcao == "4":
    if num2 == 0:
        print("Erro: Divisão por zero!")
        exit()
    resultado = num1 / num2
    operacao = "/"
else:
    print("Operação inválida.")
    exit()

# Exibe o resultado da operação
print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")

# Verifica se é inteiro ou decimal
if resultado == int(resultado):
    tipo = "inteiro"
else:
    tipo = "decimal"

# Verifica se é par ou ímpar (apenas se for inteiro)
if tipo == "inteiro":
    if int(resultado) % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"
else:
    par_impar = "não se aplica (número decimal)"

# Verifica se é positivo ou negativo
if resultado > 0:
    sinal = "positivo"
elif resultado < 0:
    sinal = "negativo"
else:
    sinal = "zero (neutro)"

# Exibe as análises
print(f"O número é {tipo}, {par_impar} e {sinal}.")