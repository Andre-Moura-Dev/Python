numero_fatorial = int(input("Informe um número inteiro positivo: "))

def fatorial_loop(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

resultado = fatorial_loop(numero_fatorial)
print(f"O fatorial de {numero_fatorial} é {resultado}")
