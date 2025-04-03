produtos = [
    {'id': 1, "nome": "Arroz", "preco": 4.50, "estoque": 100},
    {'id': 2, "nome": "Feijão", "preco": 7.20, "estoque": 90},
    {'id': 3, "nome": "Macarrão", "preco": 5.10, "estoque": 110},
    {'id': 4, "nome": "Café", "preco": 6.90, "estoque": 70},
    {'id': 5, "nome": "Açúcar", "preco": 4.10, "estoque": 88}
]

carrinho = []

def mostrar_produtos():
    print("\n --- PRODUTOS DISPONÍVEIS ---")
    for produto in produtos:
        print(f"ID: {produto['id']} | {produto['nome']} | R${produto['preco']: .2f} | Estoque: {produto['estoque']}")
        
def adicionar_carrinho():
    mostrar_produtos()
    try:
        id_produto = int(input("\n Informe o ID do produto que deseja adicionar: "))
        quantidade = int(input("Digite a quantidade: "))
        
        produto_encontrado = None
        for produto in produtos:
            if produto['id'] == id_produto:
                produto_encontrado = produto
                break
            
        if produto_encontrado:
            if quantidade <= produto_encontrado['estoque']:
                
                item_encontrado = None
                for item in carrinho:
                    if item['id'] == id_produto:
                        item_encontrado = item
                        break
                    
                if item_encontrado:
                    item_encontrado['quantidade'] += quantidade
                    
                else:
                    carrinho.append({
                        'id': produto_encontrado['id'],
                        'nome': produto_encontrado['nome'],
                        'preco': produto_encontrado['preco'],
                        'quantidade': quantidade
                    })
                    
                produto_encontrado["estoque"] -= quantidade
                print(f"{quantidade} {produto_encontrado['nome']}(s) adicionado(s) ao carrinho!")
                
            else:
                print("Quantidade indisponível em estoque!")
                
        else:
            print("Produto não encontrado!")
            
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")
        

def ver_carrinho():
    if not carrinho:
        print("\n Seu carrinho está vazio")
        return
    
    print("\n--- SEU CARRINHO ---")
    total = 0
    for item in carrinho:
        subtotal = item['preco'] * item['quantidade']
        print(f"{item['preco']} | {item['quantidade']} x R${item['preco']: .2f} = R${subtotal: .2f}")
        total += subtotal
        
    print(f"\n TOTAL: R${total: .2f}")
    
def finalizar_compra():
    if not carrinho:
        print("\n Seu carrinho está vazio!")
        return
    
    ver_carrinho()
    print("\n Compra finalizada com sucesso!")
    carrinho.clear()
    
def menu_principal():
    while True:
        print("\n--- MERCADO PYTHON ---")
        print("1. Ver produtos")
        print("2. Adicionar ao carrinho")
        print("3. Ver carrinho")
        print("4. Finalizar compra")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            mostrar_produtos()
        elif opcao == '2':
            adicionar_carrinho()
        elif opcao == '3':
            ver_carrinho()
        elif opcao == '4':
            finalizar_compra()
        elif opcao == '5':
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Opção Inválida. Tente Novamente")
            
if __name__ == "__main__":
    menu_principal()