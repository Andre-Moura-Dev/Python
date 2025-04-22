def entrada_dados():
    nome = input("Informe o seu nome: ")
    altura = float(input("Informe a sua altura: "))
    peso = float(input("Informe o seu peso: "))
    return nome, altura, peso

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Imc: {imc:.2f}")
    
    if imc < 18.5:
        print("Magro.")
    elif imc < 24.9:
        print("Normal.")
    elif imc < 29.9:
        print("Sobrepeso.")
    else:
        print("Obesidade.")
        
def sair():
    print("Saindo...")
    exit()
    
def main():
    nome, altura, peso = entrada_dados()
    
    dados = [nome, altura, peso]
    
    for dado in dados:
        print(dado)
        
    calcular_imc(peso, altura)