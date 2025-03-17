import random

def jogo_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    
    print("Bem-vindo ao Pedra, papel e tesoura!")
    
    while True:
        jogador = input("Escolha pedra, papel ou tesoura para jogar (ou 'sair' para encerrar): ").lower()
        
        if jogador == "sair":
            print("Obrigado por jogar!")
            break
            
        if jogador not in opcoes:
            print("Escolha inválida! Tente novamente.")
            continue
        
        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador}")
        
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
            (jogador == "papel" and computador == "pedra") or \
            (jogador == "tesoura" and computador == "papel"):
                print("Voçê venceu")
        else:
            print("O computador venceu!")

if __name__ == "main":
    jogo_pedra_papel_tesoura()