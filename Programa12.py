def entrada():
    nome = input("Informe o seu nome: ")
    peso = float(input("Informe o seu peso ( em kg): "))
    altura = float(input("Informe a sua altura (em metros): "))
    
    return nome, peso, altura

def calcular_IMC(peso, altura):
    imc = peso / (altura * 2)
    print(f"Imc: {imc:.2f}")
    
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 24.9:
        print("Peso Normal")
    elif imc < 29.9:
        print("Obesidade")
    elif imc < 34.9:
        print("Obesidade Grau 1")
    elif imc < 39.9:
        print("Obesidade Grau 2")
    else:
        print("Obesidade Mórbida")
        
def sair():
    print("Saindo...")
    exit()
    
def main():
    nome, peso, altura = entrada()
    
    dados = {
        "Nome": nome,
        "Peso": peso,
        "Altura": altura
    }
    
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
        
    calcular_IMC(peso, altura)