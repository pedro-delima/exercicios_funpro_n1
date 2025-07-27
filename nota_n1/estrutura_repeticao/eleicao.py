# Programa para simular uma eleição com 3 candidatos

# Inicialização dos votos
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

# Solicita o número de eleitores
total_eleitores = int(input("Informe o número total de eleitores: "))

# Votação
print("\nEscolha seu candidato digitando o número correspondente:")
print("1 - Candidato 1")
print("2 - Candidato 2")
print("3 - Candidato 3")

for i in range(total_eleitores):
    voto = int(input(f"Eleitor {i+1}, digite seu voto: "))

    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido! Voto não contabilizado.")

# Exibe o resultado final
print("\nResultado da eleição:")
print(f"Candidato 1: {votos_candidato1} voto(s)")
print(f"Candidato 2: {votos_candidato2} voto(s)")
print(f"Candidato 3: {votos_candidato3} voto(s)")