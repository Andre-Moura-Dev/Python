def entrada():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    curso = input("Digite seu curso: ")
    return nome, idade, curso

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def sair():
    print("Saindo do programa...")
    exit()

def main():
    nome, idade, curso = entrada()
    notas = []
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar nota")
        print("2 - Calcular média")
        print("3 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            print(f"Nota {nota} adicionada com sucesso!")
        elif opcao == '2':
            media = calcular_media(notas)
            print(f"\nNome: {nome}")
            print(f"Idade: {idade}")
            print(f"Curso: {curso}")
            print(f"Média: {media:.2f}")
        elif opcao == '3':
            sair()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()