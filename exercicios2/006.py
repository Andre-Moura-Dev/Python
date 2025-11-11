def contar_vogais(texto):
    texto = texto.lower()
    vogais = 'aeiou'
    cont = 0
    
    for caractere in  texto:
        if caractere in vogais:
            cont += 1
    return cont
frase = input("Informe um frase: ")
numero_vogais = contar_vogais(frase)
print(f"A frase '{frase}' tem {numero_vogais} vogal(s)")