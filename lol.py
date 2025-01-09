import random

def jogo_advinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

    # Gerar um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                acertou = True
        except ValueError:
            print("Por favor, digite um número válido.")

    print("Fim do jogo!")

# Executar o jogo
jogo_advinhacao()