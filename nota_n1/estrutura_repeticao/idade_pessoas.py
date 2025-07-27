# Programa para calcular a média de idade de uma turma e classificá-la

# Solicita o número de pessoas
n = int(input("Informe o número de pessoas na turma: "))

soma_idades = 0

# Coleta as idades e soma
for i in range(n):
    idade = int(input(f"Informe a idade da pessoa {i+1}: "))
    soma_idades += idade

# Calcula a média
media = soma_idades / n

# Classifica a turma de acordo com a média de idade
if media >= 0 and media <= 25:
    classificacao = "jovem"
elif media <= 60:
    classificacao = "adulta"
else:
    classificacao = "idosa"

# Exibe os resultados
print(f"\nA média de idade da turma é {media:.2f}.")
print(f"A turma é considerada {classificacao}.")
