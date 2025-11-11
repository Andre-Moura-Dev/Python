# Entrada de Dados
num_inteiro_positivo = int(input("Informe um número inteiro positivo: "))

# Contador da soma
soma = 0

# Looping para somar os numeros
for i in range(1, num_inteiro_positivo + 1):
    soma += i

# Exibe o resultado
print(f"A soma de 1 até {num_inteiro_positivo} é {soma}")