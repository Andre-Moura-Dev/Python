nomes = ["André", "João", "Maria", "Alice", "André", "Maria"]

contador_nomes = {}

for nome in nomes:
    if nome in contador_nomes:
        contador_nomes[nome] += 1
    else:
        contador_nomes[nome] = 1
        
for nome, quantidade in contador_nomes.items():
    print(f"{nome}: {quantidade} vezes")