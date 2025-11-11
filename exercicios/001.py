def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9


print("Calculadora temperatura: \n")
print("1. Celsisus para fahrenheit")
print("2. fahrenheit para celsius")

opcao = input("Escolha a sua opção: (1 ou 2): ")
valor = float(input("Informe a temperatura: "))

if opcao == 1:
    print(f"{valor}ºC = {celsius_to_fahrenheit(valor): .2f}ºF")
elif opcao == 2:
    print(f"{valor}ºF = {fahrenheit_to_celsius(valor): .2f}ºC")