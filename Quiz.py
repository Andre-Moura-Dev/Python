def run_quiz():
    print("Bem-vindo ao Quiz!")
    print("Responda às seguintes perguntas: ")
    
    questoes = [
        {
            "pergunta": "Qual a capital do brasil?",
            "opções": ["A) Rio de Janeiro", "B) Brasília", "C) São Paulo", "D) Salvador"],
            "resposta": "B"
        },
        {
            "pergunta": "Quantos planetas existem no sistema solar?",
            "opções": ["A) 7", "B) 8", "C) 9", "D) 10"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é o maior orgão do corpo humano?",
            "opções": ["A) Coração", "B) Cérebro", "C) Rim", "D) Pele"],
            "resposta": "D"
        },
        {
            "pergunta": "Qual é a linguagem de programação usada em sites da Web?",
            "opções": ["A) PHP", "B) Java", "C) Python", "D) JavaScript"],
            "resposta": "D"
        }
    ]
    
    score = 0
    
    for questao in questoes:
        print("\n" + questao["pergunta"])
        for opcao in questao["opcao"]:
            print(opcao)
            
        resposta = input("Sua resposta (A/B/C/D): ").upper()
        
        if resposta == questao["resposta"]:
            print("Correto!")
            score += 1
        else:
            print(f"Incorreto! A resposta correta é {questao, 'resposta'}")
    print(f"\n Quiz concluído! Seu score final: {score}/ {len(questoes)}")
    
    if score == len(questoes):
        print("Parabéns! Você acertou todas!")
    elif score >= len(questoes) / 2:
        print("Bom trabalho!")
    else:
        print("Você pode melhorar. Tente novamente!")
        
# Executar o quiz
if __name__ == "__main__":
    run_quiz()