# Função tabuada com o loop for
def tabuada(numero):
    print(f"Tabuada do {numero}: ")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

# Receber o número digitado pelo usuário        
numero_usuario = int(input("Informe um número para ver a tabuada: "))
tabuada(numero_usuario)