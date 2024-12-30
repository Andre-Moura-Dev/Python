def multiplicacao_lista(lista):
    multiplicacao = 0
    for numero in lista:
        multiplicacao *= numero
        return multiplicacao
    
numeros = [1, 2, 3, 4, 5]
resultado = multiplicacao_lista(numeros)
print(f"A multiplicação dos números é: {resultado}")