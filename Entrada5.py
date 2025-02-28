frutas = ["Maçã", "Uva", "Pêra", "Morango", "Abacaxi", "Pêra", "Maçã"]

contador_frutas = {}

for fruta in frutas:
    if fruta in contador_frutas:
        contador_frutas[fruta] += 1
    else:
        contador_frutas[fruta] = 1
        
for fruta, quantidade in contador_frutas.items():
    print(f"{frutas}: {quantidade} vezes")