# Programa para registrar temperaturas e calcular menor, maior e média

temperaturas = []

print("Digite as temperaturas. Digite 'sair' para finalizar.\n")

while True:
    entrada = input("Informe uma temperatura (ou 'sair' para encerrar): ").strip().lower()

    if entrada == "sair":
        break

    try:
        temp = float(entrada)
        temperaturas.append(temp)
    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'sair'.")

# Verifica se foram inseridas temperaturas
if len(temperaturas) > 0:
    menor = min(temperaturas)
    maior = max(temperaturas)
    media = sum(temperaturas) / len(temperaturas)

    print("\nResultados:")
    print(f"Menor temperatura: {menor:.2f}°")
    print(f"Maior temperatura: {maior:.2f}°")
    print(f"Média das temperaturas: {media:.2f}°")
else:
    print("\nNenhuma temperatura foi informada.")