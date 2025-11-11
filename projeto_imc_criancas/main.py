import struct
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from imc_utils import Dados  # Certifique-se de que a classe está com a inicial maiúscula conforme refatorado

FORMATO_REGISTRO = '30s 11s 4s f f i'  # nome, nasc, genero, peso, altura, int extra
TAMANHO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)

def ler_dados_binario(caminho_arquivo):
    """
    Lê dados de um arquivo binário e retorna uma string com os dados formatados.
    """
    dados_lidos = []

    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            while True:
                registro = arquivo.read(TAMANHO_REGISTRO)
                if not registro:
                    break

                try:
                    nome_raw, nasc_raw, genero_raw, peso, altura, _ = struct.unpack(FORMATO_REGISTRO, registro)
                    nome = nome_raw.decode('utf-8').strip('\x00')
                    nasc = nasc_raw.decode('utf-8').strip('\x00')
                    genero = genero_raw.decode('utf-8').strip('\x00')

                    pessoa = Dados(nome, nasc, genero, peso, altura)
                    dados_lidos.append(str(pessoa))
                except Exception as e:
                    dados_lidos.append(f"Erro ao processar registro: {e}")
    except FileNotFoundError:
        return "Arquivo não encontrado."
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

    return "\n".join(dados_lidos)

def abrir_arquivo():
    """
    Abre um diálogo para seleção de arquivo e exibe o conteúdo formatado.
    """
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos binários", "*.bin")])
    if not caminho:
        return

    conteudo = ler_dados_binario(caminho)
    texto_saida.delete('1.0', tk.END)
    texto_saida.insert(tk.END, conteudo)

# Interface Gráfica
def iniciar_interface():
    global texto_saida
    janela = tk.Tk()
    janela.title("Leitor de Dados IMC")
    janela.geometry("600x500")

    botao = tk.Button(janela, text="Abrir Arquivo .bin", command=abrir_arquivo)
    botao.pack(pady=10)

    texto_saida = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=70, height=25)
    texto_saida.pack(padx=10, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_interface()
