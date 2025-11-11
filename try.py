carros = []

def cadastrarCarros():
    marca = input("Informe a marca do carro: ")
    modelo = input("Informe o modelo de carro: ")
    ano_fabricacao = int(input("Informe o ano de fabricação: "))
    preco = float(input("Informe o preço: "))
    
    carro = {"id": len(carros) + 1, "Marca": marca, "Modelo": modelo, "Ano Fabricação": ano_fabricacao, "Preço": preco}
    carros.append(carro)
    print("Carro cadastrado com sucesso!")
    
    return marca, modelo, ano_fabricacao, preco

def listarCarros():
    if not carros:
        print("Nenhum carro cadastrado!")
    else:
        for c in carros:
            print(c['marca'], c['modelo'], c['ano_fabricacao'], c['preco'])
        print()
        
def atualizarCarros():
    id_carro = int(input("Digite o ID do carro que deseja atualizar: "))
    
    for c in carros:
        if c['id'] == id_carro:
            c['marca'] = input("Nova Marca: ")
            c['modelo'] = input("Novo Modelo: ")
            c['ano_fabricacao'] = input("Novo Ano Fabricação: ")
            c['preco'] = input("Novo Preço: ")
            print("Carro atualizado com sucesso!")
            return
    print("Nenhum Carro Encontrado!!!")
        
def deletarCarros():
    id_carro = int(input("Digite o ID do carro que deseja deletar: "))
    
    for c in carros:
        if c[''] == id_carro:
            carros.remove(c)
            print("Carro atualizado com sucesso!")
            return
    print("Nenhum Carro Encontrado!")
    
def sair():
    print("Saindo...")
    exit()
    
def main():
    while True:
        print("1 - Cadastrar Carros: ")
        print("2 - Listar Carros: ")
        print("3 - Deletar Carros: ")
        print("4 - Atualizar Carros: ")
        print("5 - Sair: ")
        opcao = input("Informe a sua escolha: ")
        
        if opcao == '1':
            cadastrarCarros()
        elif opcao == '2':
            listarCarros()
        elif opcao == '3':
            deletarCarros()
        elif opcao == '4':
            atualizarCarros()
        elif opcao == '5':
            sair()
        else: