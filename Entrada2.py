numeros = [43, 53, 23, 76, 87, 87, 53, 23]

contador_numeros = {}

for numero in numeros:
    if numero in contador_numeros:
        contador_numeros[numero] += 1
    else:
        contador_numeros[numero] = 1
        
for numero, quantidade in contador_numeros.items():
    print(f"{numeros}: {quantidade} vezes")