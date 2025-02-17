nomes = ["André", "João", "Maria", "Alice", "André", "Maria"] # Array de nomes para o dicionário

contador_nomes = {} # Dicionário para armazenar nomes

# Lopping para percorrer os nomes dentro do dicionário
for nome in nomes:
    if nome in contador_nomes:
        contador_nomes[nome] += 1
    else:
        contador_nomes[nome] = 1
        
for nome, quantidade in contador_nomes.items():
    print(f"{nome}: {quantidade} vezes") # Printar os nomes para a saída