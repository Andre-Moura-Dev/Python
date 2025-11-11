import random

print("Olá, bem vindo ao jogo de advinhação \n")
print("Tente advinhar um número de 1 a 100 \n")

numero_secreto = random.randint(1, 100)

tentativas = 0

while True:
    chute = int(input("Informe o seu palpite:")) 
    
    if chute < numero_secreto:
        print("Muito baixo! Tente Novamente.")
    elif chute > numero_secreto:
        print("Muito Alto! Tente Novamente.")
    else:
        print(f"Parabéns! Voce acertou o numero em {tentativas} tentaivas")