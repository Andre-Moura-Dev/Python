def dados_Pessoas():
    nome = input("Informe o seu nome: ")
    peso = float(input("Informe o seu peso: "))
    altura = float(input("Informe a sua altura: "))
    
    return nome, peso, altura

def calcular_IMC(peso, altura):
    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.2f}")
    
    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc <= 24.9:
        print("Peso Normal")
    elif imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30:
        print("Obesidade")
    
def main():
    nome, peso, altura = dados_Pessoas()
    
    dados = [nome, peso, altura]
    
    for dado in dados:
        print(dado)
        
    calcular_IMC(peso, altura)
    
if __name__ == "__main__":
    main()