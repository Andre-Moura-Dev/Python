import struct
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from imc_utils import dados

def ler_dados_binario(caminho_arquivo):
    form = '30s 11s 4s f f i'
    tam = struct.calcsize(form)
    dados_lidos = []

    with open(caminho_arquivo, 'rb') as f:
        while True:
            record_data = f.read(tam)
            if not record_data:
                break
            record = struct.unpack(form, record_data)
            nome = record[0].decode().strip('\x00')
            nasc = record[1].decode().strip('\x00')
            genero = record[2].decode().strip('\x00')
            peso = record[3]
            altura = record[4]
            pessoa = dados(nome, nasc, genero, peso, altura)
            dados_lidos.append(str(pessoa))
    
    return "\n".join(dados_lidos)

def abrir_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos binários", "*.bin")])
    if not caminho:
        return
    try:
        conteudo = ler_dados_binario(caminho)
        texto_saida.delete('1.0', tk.END)
        texto_saida.insert(tk.END, conteudo)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o arquivo: {e}")

janela = tk.Tk()
janela.title("Leitor de Dados IMC")
janela.geometry("600x500")

botao = tk.Button(janela, text="Abrir Arquivo .bin", command=abrir_arquivo)
botao.pack(pady=10)

texto_saida = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=70, height=25)
texto_saida.pack(padx=10, pady=10)

janela.mainloop()
