nota_1 = float(input("Digite a 1ª Nota: "))
nota_2 = float(input("Digite a 2ª Nota: "))
nota_3 = float(input("Digite a 3ª Nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

while True:
    nome = input("Informe o nome do Aluno: ")
    break

if media >= 6:
    print("Aprovado")
elif media < 6:
    print("Reprovado")
    
print("O aluno foi", media)