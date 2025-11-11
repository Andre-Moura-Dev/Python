pessoas = []

def cadastrarPessoas():
    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))
    sexo = input("Informe o seu sexo (M ou F): ")
    altura = float(input("Informe a sua altura (em metros): "))
    
    pessoa = {"id": len(pessoas) + 1, "nome": nome, "idade": idade, "sexo": sexo, "altura": altura}
    pessoas.append(pessoa)
    print("Pesssoa cadastrada com sucesso!\n")
    
def listarUsuarios():
    if not pessoas:
        print("Nenhuma pessoa cadastrada!\n")
    else:
        for p in pessoas:
            print(f"ID: {p['id']}, Nome: {p['nome']}, Idade: {p['idade']}, Sexo: {p['sexo']}, Altura: {p['altura']}")
        print()
        
def atualizarPessoas():
    id_pessoa = int(input("Informe o ID da pessoa que deseja atualizar: "))
    for p in pessoas:
        if p['id'] == id_pessoa:
            p['nome'] = input("Novo nome: ")
            p['idade'] = input("Nova Idade: ")
            p['sexo'] = input("Novo Sexo: ")
            p['altura'] = input("Nova altura: ")
            print("Pessoa atualizada com sucesso!\n")
            return
    print("Nenhuma pessoa encontrada!\n")
    
def deletarPessoas():
    id_pessoa = int(input("Informe o ID da pessoa que deseja deletar: "))
    for p in pessoas:
        if['id'] == id_pessoa:
            pessoas.remove(p)
            print("Pessoa deletada com sucesso!\n")
            return
    print("nenhuma pessoa encontrada!\n")
    
def sair():
    print("Saindo...")
    exit()
    
def main():
    while True:
        print("1 - Cadastrar Pessoas")
        print("2 - Listar Pessoas")
        print("3 - Atualizar Pessoas")
        print("4 - Deletar Pessoas")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrarPessoas()
        elif opcao == '2':
            listarUsuarios()
        elif opcao == '3':
            atualizarPessoas()
        elif opcao == '4':
            deletarPessoas()
        elif opcao == '5':
            sair()
            break
        else:
            print("Opção Inválida. Tente Novamente!\n")
            
if __name__ == "__main__":
    main()