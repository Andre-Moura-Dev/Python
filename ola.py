def calcular_media(notas):
    soma = sum(notas)
    media = soma /len(notas)
    return media

notas = []

for i in range(5):
    nota = float(input(f"Informe as notas do aluno {i + 1}: "))
    notas.append(nota)
    
media = calcular_media(notas)

print(f"A média das notas é {media:2.f}")

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")