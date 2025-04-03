# função Entrada de dados
def entrada():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura"))
    curso = input("Digite seu curso: ")
    return nome, idade, curso, peso, altura

# calcular imc
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"\nIMC: {imc:.2f}")
    
    if imc < 18.5:
        print("Classificação: Magreza")
    elif imc < 24.9:
        print("Classificação: Normal")
    elif imc < 29.9:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obesidade")        
    

# calcular média
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Sair
def sair():
    print("Saindo do programa...")
    exit()

# função principal
def main():
    nome, idade, curso, peso, altura = entrada()
    notas = []
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar nota")
        print("2 - Calcular média")
        print("3 - Calcular imc")
        print("4 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            quantidade = int(input("Quantas notas deseja adicionar? "))
            for i in range(quantidade):
                nota = float(input(f"Informe a nota {i + 1}: "))
                notas.append(nota)
            print(f"{quantidade} notas adicionadas com sucesso!!!")
        elif opcao == '2':
            media = calcular_media(notas)
            print(f"\nNome: {nome}")
            print(f"Idade: {idade}")
            print(f"Curso: {curso}")
            print(f"Média: {media:.2f}")
            
        elif opcao == '3':
            calcular_imc(peso, altura)
            
            if media >= 7:
                print("Aprovado!")
            else:
                print("Reprovado!")
            
        elif opcao == '4':
            sair()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()