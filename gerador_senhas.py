# Importacoes
import random
import string

def gerar_senha():
    print("Bem-vindo ao gerador de senhas!")
    
    # Configuracoes de Senha
    comprimento = int(input("Informe o comprimento desejado para a senha: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir minúsculas? (s/n): ").lower() == 's'
    
    # Conjunto Caracteres
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    if incluir_minusculas:
        caracteres += string.ascii_letters
        
    # Geração de senha
    if not caracteres:
        print("Você precisa selecionar pelo menos um tipo de caracter")
        return
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f"Sua senha gerada é: {senha}")

# Chama a função gerar senha
gerar_senha()    