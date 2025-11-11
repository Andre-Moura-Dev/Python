numero1 = int(input("Informe o 1º número: \n"))
numero2 = int(input("Informe o 2º número: \n"))
numero3 = int(input("Informe o 3º número: \n"))

if numero1 > numero2 and numero1 > numero3:
    print(f"O maior número é: {numero1}")
elif numero2 > numero3:
    print(f"O maior número é: {numero2}")
elif numero1 == numero2 == numero3:
    print("Os números são iguais")
else:
    print(f"O maior número é: {numero3}")