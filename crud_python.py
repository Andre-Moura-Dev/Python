alunos = []

def cadastrar_aluno():
    nome = input("Informe o nome: ")
    idade = int(input("Informe a sua idade: "))
    matricula = input("Informe a sua matricula: ")
    curso = input("Informe o curso do aluno: ")
    
    aluno = {"id": len(alunos) + 1, "nome": nome, "idade": idade, "matricula": matricula, "curso": curso}
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")
    
def listar_usuarios():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
    else:
        for a in alunos:
            print(f"ID: {a['id']}, Nome: {a['nome']}, Idade: {a['idade']}, Matrícula: {a['matricula']}, Curso: {a['curso']}")
        print()
        
def atualizar_aluno():
    id_aluno = int(input("Digite o ID do aluno que deseja atualizar: "))
    for a in alunos:
        if a['id'] == id_aluno:
            a['nome'] = input("Novo nome: ")
            a['idade'] = input("Nova idade: ")
            a['matricula'] = input("Nova matrícula: ")
            a['curso'] = input("Novo curso: ")
            print("Aluno atualizado com sucesso!\n")
            return    
    print("Nenhum aluno encontrado!\n")
    
def deletar_aluno():
    id_aluno = int(input("Informe o ID do aluno que deseja deletar: "))
    for a in alunos:
        if a['id'] == id_aluno:
            alunos.remove(a)
            print("Aluno deletado com sucesso!\n")
            return
    print("Aluno não encontrado.\n")
    
def menu():
    while True:
        print("1 - Cadastrar Alunos")
        print("2 - Listar Alunos")
        print("3 - Atualizar Alunos")
        print("4 - Deletar Alunos")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            deletar_aluno()
        elif opcao == '5':
            print("Sair")
            break
        else:
            print("Opção inválida\n")      

menu()
