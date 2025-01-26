def imprimir_tabuleiro(tabuleiro):
    for i in range(3):
        print(' | '.join(tabuleiro[i]))
        if i < 2:
            print("---------")
            
def verificar_vencedor(tabuleiro):
    
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]
        
    if tabuleiro[0][0] == tabuleiro[1][i] == tabuleiro[2][2] != '':
            return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '':
            return tabuleiro [0][2]
        
    return None

def tabuleiro_cheio(tabuleiro):
    for row in tabuleiro:
        if ' ' in row:
            return False
    return True

def jogar():
    
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    
    while True:
        
        imprimir_tabuleiro(tabuleiro)
        
        print(f"Jogador {jogador_atual}, escolha sua posição (linha e coluna):")
        linha, coluna = map(int, input("Informe a linha  e a coluna (0-2) separadas por espaço: ").split())
        
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Posição já ocupada, tente novamente.")
            continue
        
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {vencedor} venceu!")
            break
        
        if tabuleiro_cheio(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        
jogar()