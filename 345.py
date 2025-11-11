from datetime import datetime, timedelta

produtos = []

def cadastrarProdutos():
    nome = input("Informe o nome do produto: ")
    qtd = int(input("Informe a quantidade do produto: "))
    preco = float(input("Informe o preço do produto: "))
    data_str = calcularDataValidade()
    
    produto = {"id": len(produtos) + 1, "Nome": nome, "Qtd": qtd, "Preço": preco, "Data_Str": data_str}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!\n")
    
def listarProdutos():
    if not produtos:
        print("Nenhum produto cadastrado!")
    else:
        for p in produtos:
            print(f"ID: {p['id']}, Nome: {p['nome']}, Qtd: {p['qtd']}, Preço: {p['preco']}, Data_Str: {p['data_str']}")
        print()
        
def atualizarProdutos():
    id_produto = int(input("Informe o ID do produto que deseja atualizar: "))
    
    for p in produtos:
        if p ['id'] == id_produto:
            p['nome'] = input("Novo Nome: ")
            p['qtd'] = input("Nova Quantidade: ")
            p['preco'] = input("Novo Preço: ")
            p['data_str'] = input("Nova Data: ")
            print("Produto atualizado com sucesso!\n")
            return
    print("Erro ao atualizar produto!\n")
    
def deletarProdutos():
    id_produto = int(input("Informe o ID do produto que deseja deletar: "))
    for p in produtos:
        if p['id'] == id_produto:
            produtos.remove(p)
            print("Produto deletado com sucesso!\n")
            return
    print("Erro ao deletar produto!\n")
    
def calcularDataValidade(data_fabricacao_str, dias_validade):
    data_fabricacao_str = input("Informe a data de fabricação (DD/MM/AAAA): ")
    dias_validade = int(input("Informe a validade em dias: "))
    data_fabricacao = datetime.strptime(data_fabricacao_str, "%d/%m/%Y")
    data_validade = data_fabricacao + timedelta(days=dias_validade)
    return data_validade.strftime("%d/%m/%Y")

def sair():
    print("Saindo...")
    exit()
    
def menu():
    while True:
        print("1 - Cadastrar Produtos")
        print("2 - Listar Produtos")
        print("3 - Atualizar produtos")
        print("4 - Deletar Produtos")
        print("5 - Calcular Data Validade")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrarProdutos()
        elif opcao == '2':
            listarProdutos()
        elif opcao == '3':
            atualizarProdutos()
        elif opcao == '4':
            deletarProdutos()
        elif opcao == '5':
            calcularDataValidade(data_fabricacao_str=0, dias_validade=0)
        elif opcao == '6':
            sair()
            break
        else:
            print("opção Inválida")
menu()