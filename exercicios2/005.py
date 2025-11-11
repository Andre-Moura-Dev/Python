def gerar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    inversao = texto[::-1]
    
    if texto == inversao:
        return True
    else:
        return False
    
entrada = input("Informe uma frase ou palavra: ")
if gerar_palindromo(entrada):
    print("A entrada é um palíndromo!")
else:
    print("A entrada não é um palíndromo!")