nome = str(input("Informe o seu nome: "))
idade = int(input("Informe a sua idade: "))

if idade == 18:
    print("Idade Normal")
elif idade > 18:
    print("Maior de idade")
elif idade < 18:
    print("Menor de idade")