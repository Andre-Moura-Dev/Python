def entrada_dados():
    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))
    curso = input("Informe o seu curso: ")
    
    return nome, idade, curso

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def sair():
    print("Saindo do Programa...")
    exit()
    
def main():
    nome, idade, curso = entrada_dados()
    notas = []
    
    while True:
        print("\n Escolha uma opção: ")
        print("1 - Adicionar Notas")
        print("2 - Calcular Média")
        print("3 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            nota = float(input("Informe a sua nota: "))
            notas.append(nota)
        elif opcao == '2':
            media = calcular_media(notas)
            print(f"\n Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Curso: {curso}")
            print(f"Média: {media: 2.f}")
        elif opcao == '3':
            sair()
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == " __main__ ":
    main()