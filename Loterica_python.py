import random

def fazer_aposta():
    print("Faça sua aposta (6 números de 1 a 60): ")
    aposta = set()
    
    while len(aposta) < 6:
        try:
            numero = int(input(f"Digite o {len(aposta) + 1}º número: "))
            if 1 <= numero <= 60:
                if numero in aposta:
                    print("Número já escolhido. Tente outro!")
                else:
                    aposta.add(numero)
            else:
                print("Número fora do intervalo. Escolha entre 1 e 60")
        except ValueError:
            print("Entrada inválida. Digite um número.")
            
    return aposta

def sortear_numeros():
    return set(random.sample(range(1,60), 6))

def verificar_resultado(aposta, sorteio):
    acertos = aposta & sorteio
    quntidade_acertos = len(acertos)
    
    print(f"\n Números sorteados: {sorted(sorteio)}")
    print(f" Sua aposta: {sorted(aposta)}")
    print(f" Você acertou {quntidade_acertos} números(s): {sorted(acertos)}")
    
    if quntidade_acertos == 6:
        print("Parabéns! Voçê ganhou o prêmio máximo!")
    elif quntidade_acertos == 5:
        print("Quase lá! Voçê acertou a Quina.")
    elif quntidade_acertos == 4:
        print("Boa! Voçê acertou a Quadra.")
    else:
        print("Infelizmente, não foi dessa vez.")
        
def main():
    print("Bem-vindo à lotérica online")
    aposta = fazer_aposta()
    sorteio = sortear_numeros()
    verificar_resultado(aposta, sorteio)
    
if __name__ == "__main__":
    main()