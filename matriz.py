matriz = []

print("Preencha a matriz 3x3:")
for i in range(3):
    linha = []
    for j  in range(3):
        valor = int(input(f"Informe o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
    
print("\n Matriz 3x3:")
for linha in matriz:
    print(linha)