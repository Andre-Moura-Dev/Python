# 📊 Análise Estática e Refatoração de Código: Projeto IMC Infantil em Python

## 🔗 Projeto Selecionado

**Nome:** Leitor de Arquivo Binário com Cálculo de IMC Infantil  
**Descrição:** Interface gráfica que lê registros binários contendo informações de crianças (nome, nascimento, gênero, peso, altura) e calcula o IMC com base em uma tabela específica.  
**Linguagem:** Python  
**Interface:** Tkinter  
**Repositório:** _Projeto local desenvolvido por [Seu Nome]_  

---

## 🧪 Parte 1: Análise Estática do Código

### 🔍 Ferramentas Utilizadas

- [`pylint`](https://pylint.pycqa.org): análise de estilo e boas práticas.
- [`radon`](https://radon.readthedocs.io): complexidade ciclomática e índice de manutenibilidade.

> Para execução:
> ```
> pip install pylint radon
> pylint interface.py
> radon cc interface.py -a
> radon mi interface.py
> ```

---

### 📈 Resultados da Análise Estática

#### 📌 1. `dados.py`

- **Complexidade Ciclomática** (`radon cc`):

  | Função              | Complexidade |
  |---------------------|--------------|
  | `get_target`        | 6            |
  | `__str__`           | 3            |
  | `calc_idade`        | 1            |

  > **Média:** 3.3 – Complexidade moderada.

- **Índice de Manutenibilidade (`radon mi`)**:
  
