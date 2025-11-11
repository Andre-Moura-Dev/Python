from fpdf import FPDF
import numpy as np

# Configurar PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Lista 02 - Algebra Linear Aplicada", ln=True, align='C')
pdf.ln(5)
pdf.set_font("Helvetica", "", 12)

def escrever_titulo(titulo):
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, titulo, ln=True)
    pdf.set_font("Helvetica", "", 12)

def escrever_texto(texto):
    for linha in texto.split('\n'):
        if linha.strip() == "":  # pular linhas vazias extras
            pdf.ln(4)
        else:
            pdf.cell(0, 8, linha, ln=True)

def matriz_para_str(matriz, inteiro=False):
    if inteiro:
        return '\n'.join([' '.join(f'{int(elem):6}' for elem in linha) for linha in matriz])
    else:
        return '\n'.join([' '.join(f'{elem:8.2f}' for elem in linha) for linha in matriz])

def det_2x2_passo(A, nome="A"):
    a, b = A[0]
    c, d = A[1]
    det = a*d - b*c
    passo = f"det({nome}) = ({a})×({d}) - ({b})×({c}) = {a*d:.2f} - {b*c:.2f} = {det:.2f}"
    return det, passo

def det_3x3_sarrus(A, nome="A"):
    # Repetir as duas primeiras colunas
    ext = np.column_stack((A, A[:, :2]))
    soma_pos = 0
    termos_pos = []
    soma_neg = 0
    termos_neg = []
    
    # Diagonais principais (positivas)
    for i in range(3):
        prod = ext[0, i] * ext[1, i+1] * ext[2, i+2]
        soma_pos += prod
        termos_pos.append(f"({ext[0, i]:.0f})×({ext[1, i+1]:.0f})×({ext[2, i+2]:.0f}) = {prod:.0f}")
    
    # Diagonais secundárias (negativas)
    for i in range(3):
        prod = ext[2, i] * ext[1, i+1] * ext[0, i+2]
        soma_neg += prod
        termos_neg.append(f"({ext[2, i]:.0f})×({ext[1, i+1]:.0f})×({ext[0, i+2]:.0f}) = {prod:.0f}")
    
    det = soma_pos - soma_neg
    passo = (
        f"Regra de Sarrus aplicada a {nome}:\n"
        f"Matriz expandida:\n{matriz_para_str(ext[:,:5])}\n"
        f"Diagonais principais (soma):\n  " + "\n  ".join(termos_pos) + f"\n  Soma = {soma_pos:.0f}\n"
        f"Diagonais secundárias (soma):\n  " + "\n  ".join(termos_neg) + f"\n  Soma = {soma_neg:.0f}\n"
        f"det({nome}) = {soma_pos:.0f} - {soma_neg:.0f} = {det:.0f}"
    )
    return det, passo


# === 1. Filtro de Brilho ===
escrever_titulo("1. Filtro de Brilho (Processamento de Imagens)")
I1 = np.array([[120, 200],
               [50, 180]])
I1_brilho = I1 + 40

texto1 = (
    "Passo 1: Matriz original (tons de cinza):\n"
    f"{matriz_para_str(I1, inteiro=True)}\n"
    "Passo 2: Adicionar +40 a cada pixel (operação elemento a elemento):\n"
    f"Novo pixel (1,1): 120 + 40 = {I1_brilho[0,0]}\n"
    f"Novo pixel (1,2): 200 + 40 = {I1_brilho[0,1]}\n"
    f"Novo pixel (2,1): 50 + 40 = {I1_brilho[1,0]}\n"
    f"Novo pixel (2,2): 180 + 40 = {I1_brilho[1,1]}\n"
    "Resultado:\n"
    f"{matriz_para_str(I1_brilho, inteiro=True)}"
)
escrever_texto(texto1)
pdf.ln(5)

# === 2. Comparação de Algoritmos ===
escrever_titulo("2. Comparação de Algoritmos")
A = np.array([[1.2, 1.3],
              [1.0, 0.9]])
Ax = A[0, :]  # Algoritmo X
Ave = np.mean(A, axis=0)  # média por coluna (teste)
diferenca = Ax - Ave

texto2 = (
    "Passo 1: Matriz de tempos A:\n"
    f"{matriz_para_str(A)}\n"
    "Passo 2: Calcular média por teste (coluna):\n"
    f"Teste 1: (1.2 + 1.0)/2 = {Ave[0]:.2f}\n"
    f"Teste 2: (1.3 + 0.9)/2 = {Ave[1]:.2f}\n"
    f"Média geral por teste: [{Ave[0]:.2f}, {Ave[1]:.2f}]\n"
    "Passo 3: Calcular diferença (Algoritmo X - Média):\n"
    f"[{Ax[0]}, {Ax[1]}] - [{Ave[0]:.2f}, {Ave[1]:.2f}] = [{diferenca[0]:.2f}, {diferenca[1]:.2f}]\n"
    "Interpretação:\n"
    f"Se a diferença for negativa, o Algoritmo X foi mais rápido que a média.\n"
    f"-> Teste 1: {'mais eficiente' if diferenca[0] < 0 else 'menos eficiente'}\n"
    f"-> Teste 2: {'mais eficiente' if diferenca[1] < 0 else 'menos eficiente'}\n"
    f"Conclusão: O Algoritmo X foi mais eficiente nos testes onde o valor é negativo."
)
escrever_texto(texto2)
pdf.ln(5)

# === 3. Rotação em 2D ===
escrever_titulo("3. Computação Gráfica - Rotação 2D")
R = np.array([[0, -1],
              [1,  0]])
P = np.array([[3],
              [4]])
RP = R @ P

texto3 = (
    "Passo 1: Matriz de rotação R (90° anti-horário):\n"
    f"{matriz_para_str(R, inteiro=True)}\n"
    "Passo 2: Ponto original P:\n"
    f"{matriz_para_str(P, inteiro=True)}\n"
    "Passo 3: Multiplicação R·P:\n"
    f"Nova coordenada x: (0)(3) + (-1)(4) = 0 - 4 = {RP[0,0]}\n"
    f"Nova coordenada y: (1)(3) + (0)(4) = 3 + 0 = {RP[1,0]}\n"
    "Resultado:\n"
    f"R·P = {matriz_para_str(RP, inteiro=True)}\n"
    f"Novas coordenadas: ({RP[0,0]}, {RP[1,0]})"
)
escrever_texto(texto3)
pdf.ln(5)

# === 4. Criptografia ===
escrever_titulo("4. Criptografia - Codificação de Mensagem")
K = np.array([[1, 2],
              [3, 4]])
M = np.array([[2],
              [1]])
C = K @ M

texto4 = (
    "Passo 1: Matriz-chave K:\n"
    f"{matriz_para_str(K, inteiro=True)}\n"
    "Passo 2: Vetor mensagem M:\n"
    f"{matriz_para_str(M, inteiro=True)}\n"
    "Passo 3: Multiplicação C = K·M:\n"
    f"Primeira linha: (1)(2) + (2)(1) = 2 + 2 = {C[0,0]}\n"
    f"Segunda linha: (3)(2) + (4)(1) = 6 + 4 = {C[1,0]}\n"
    "Resultado:\n"
    f"C = {matriz_para_str(C, inteiro=True)}"
)
escrever_texto(texto4)
pdf.ln(5)

# === 5. Banco de Dados - Consultas ===
escrever_titulo("5. Banco de Dados - Q1 - Q2")
Q1 = np.array([[100, 200],
               [150, 250]])
Q2 = np.array([[80, 220],
               [170, 240]])
diferenca = Q1 - Q2

texto5 = (
    "Passo 1: Matrizes de consultas:\n"
    f"Q1 (dia 1):\n{matriz_para_str(Q1, inteiro=True)}\n"
    f"Q2 (dia 2):\n{matriz_para_str(Q2, inteiro=True)}\n"
    "Passo 2: Calcular Q1 - Q2 (elemento a elemento):\n"
    f"Leitura, campo 1: 100 - 80 = {diferenca[0,0]}\n"
    f"Leitura, campo 2: 200 - 220 = {diferenca[0,1]}\n"
    f"Escrita, campo 1: 150 - 170 = {diferenca[1,0]}\n"
    f"Escrita, campo 2: 250 - 240 = {diferenca[1,1]}\n"
    "Interpretação:\n"
    f"-> Leitura: {'aumentou' if diferenca[0,0] > 0 else 'diminuiu'} no primeiro campo, "
    f"{'aumentou' if diferenca[0,1] > 0 else 'diminuiu'} no segundo.\n"
    f"-> Escrita: {'aumentou' if diferenca[1,0] > 0 else 'diminuiu'} no primeiro campo, "
    f"{'aumentou' if diferenca[1,1] > 0 else 'diminuiu'} no segundo."
)
escrever_texto(texto5)
pdf.ln(5)

# === 6. Determinante 2x2 - Independência de Dados ===
escrever_titulo("6. Determinante 2x2 - Independência de Dados")
A = np.array([[3, 5],
              [2, 4]])
detA, passo_detA = det_2x2_passo(A, "A")

texto6 = (
    "Passo 1: Matriz A:\n"
    f"{matriz_para_str(A, inteiro=True)}\n"
    "Passo 2: Calcular det(A) = a*d - b*c:\n"
    f"{passo_detA}\n"
    "Interpretação:\n"
    f"Se det(A) ≠ 0, os dados são linearmente independentes.\n"
    f"Como det(A) = {detA:.2f} {'≠ 0' if abs(detA) > 1e-10 else '= 0'}, os dados são {'independentes' if abs(detA) > 1e-10 else 'linearmente dependentes'}."
)
escrever_texto(texto6)
pdf.ln(5)

# === 7. Determinante 3x3 - Inteligência Artificial ===
escrever_titulo("7. Determinante 3x3 - Pesos de Rede Neural")
P = np.array([[2, -1, 3],
              [0,  4, 5],
              [1,  2, -2]])
detP, passo_detP = det_3x3_sarrus(P, "P")

texto7 = (
    "Passo 1: Matriz de pesos P:\n"
    f"{matriz_para_str(P, inteiro=True)}\n"
    "Passo 2: Aplicar Regra de Sarrus:\n"
    f"{passo_detP}\n"
    "Interpretação:\n"
    f"Se det(P) ≠ 0, os vetores (pesos) são linearmente independentes.\n"
    f"Como det(P) = {detP:.0f} {'≠ 0' if abs(detP) > 1e-10 else '= 0'}, os pesos são {'linearmente independentes' if abs(detP) > 1e-10 else 'linearmente dependentes'}."
)
escrever_texto(texto7)
pdf.ln(5)

# === 8. Determinante 2x2 - Análise de Custos ===
escrever_titulo("8. Determinante 2x2 - Análise de Custos")
C = np.array([[5000, 7000],
              [3000, 4000]])
detC, passo_detC = det_2x2_passo(C, "C")

texto8 = (
    "Passo 1: Matriz de custos C:\n"
    f"{matriz_para_str(C, inteiro=True)}\n"
    "Passo 2: Calcular det(C):\n"
    f"{passo_detC}\n"
    "Interpretação:\n"
    f"Se det(C) = 0, as linhas são proporcionais (custos proporcionais).\n"
    f"Como det(C) = {detC:.0f} {'= 0' if abs(detC) < 1e-10 else '≠ 0'}, os custos {'são proporcionais' if abs(detC) < 1e-10 else 'não são proporcionais'}."
)
escrever_texto(texto8)
pdf.ln(5)

# === 9. Determinante 3x3 - Tráfego de Rede ===
escrever_titulo("9. Determinante 3x3 - Tráfego de Rede")
N = np.array([[120, 80, 60],
              [100, 90, 70],
              [90, 60, 50]])
detN, passo_detN = det_3x3_sarrus(N, "N")

texto9 = (
    "Passo 1: Matriz de tráfego N:\n"
    f"{matriz_para_str(N, inteiro=True)}\n"
    "Passo 2: Aplicar Regra de Sarrus:\n"
    f"{passo_detN}\n"
    "Interpretação:\n"
    f"Se det(N) ≠ 0, os fluxos são independentes.\n"
    f"Como det(N) = {detN:.0f} {'≠ 0' if abs(detN) > 1e-10 else '= 0'}, os fluxos de rede são {'independentes' if abs(detN) > 1e-10 else 'linearmente dependentes'}."
)
escrever_texto(texto9)
pdf.ln(5)

# === 10. Determinante 3x3 - Sistema Linear ===
escrever_titulo("10. Determinante 3x3 - Sistema Linear")
S = np.array([[2, -1, 3],
              [1,  2, 1],
              [3,  1, 2]])
detS, passo_detS = det_3x3_sarrus(S, "S")

texto10 = (
    "Passo 1: Matriz do sistema S:\n"
    f"{matriz_para_str(S, inteiro=True)}\n"
    "Passo 2: Aplicar Regra de Sarrus:\n"
    f"{passo_detS}\n"
    "Interpretação:\n"
    f"Um sistema tem solução única se det(S) ≠ 0.\n"
    f"Como det(S) = {detS:.0f} {'≠ 0' if abs(detS) > 1e-10 else '= 0'}, o sistema {'possui solução única' if abs(detS) > 1e-10 else 'não possui solução única (pode ser impossível ou indeterminado)'}."
)
escrever_texto(texto10)
pdf.ln(5)

# Salvar PDF
pdf.output("Lista_02_Resolvida_Com_Passos.pdf")
print("✅ PDF com passo a passo gerado com sucesso: Lista_02_Resolvida_Com_Passos.pdf")