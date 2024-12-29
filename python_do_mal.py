# Dados

nome = str(input("Informe o seu nome: \n"))
idade = int(input("Informe a sua idade: \n"))

if idade >= 18:
    print("Maior de idade!")
elif idade < 18:
    print("Menor de Idade!")

# Soma de numeros em uma lista

def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += int(numero) 
    return soma

numeros = ['1', '2', '3', '4', '5']
resultado = soma_lista(numeros)
print(f"A soma dos números é: {resultado}")

# Subtração de numeros em uma lista

def subtracao_lista(lista):
    subtracao = 0
    for numero in lista:
        subtracao += int(numero)
    return subtracao

numeros = ['1', '2', '3', '4', '5']
resultado = subtracao_lista(numeros)
print(f"A subtracao dos números é: {resultado}")

# Media com for

#Função calcular a média das notas
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas = [] # Lista de noatas

# Receber as notas do aluno
for i in range(5):
    nota = float(input(f"Informe as notas do aluno {i + 1}: "))
    notas.append(nota)

# Calcular a média
media = calcular_media(notas)

print(f"A média das notas é: {media:2.f}")

# Verifica se está aprovado ou não
if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")