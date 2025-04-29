from datetime import datetime

class DadosInvalidosError(Exception):
    pass

class dados:
    def __init__(self, nome, nasc, genero, peso, altura):
        self.nome = nome
        self.nasc = nasc
        self.genero = genero
        self.peso = peso
        self.altura = altura

    def calcIdade(self):
        n = datetime.strptime(self.nasc, "%Y-%m-%d")
        return (datetime.now() - n).days // 365

    def getTarget(self):
        idade = self.calcIdade()
        imc = self.peso / (self.altura ** 2)

        tabela = {
            'Masc': {6: [14.5, 16.7, 18], 7: [15, 17.4, 19.1], 8: [15.6, 16.8, 20.3]},
            'Femi': {6: [14.3, 16.2, 17.4], 7: [14.9, 17.2, 18.9], 8: [15.6, 18.2, 20.3]}
        }

        if self.genero not in tabela or idade not in tabela[self.genero]:
            raise DadosInvalidosError(f"Idade ({idade}) ou gênero ({self.genero}) inválido(s).")

        limites = tabela[self.genero][idade]
        if imc < limites[0]:
            return 0
        elif imc < limites[1]:
            return 1
        elif imc < limites[2]:
            return 2
        else:
            return 3

    def __str__(self):
        try:
            target = self.getTarget()
        except DadosInvalidosError as e:
            target = f"Erro: {e}"
        return (f"Nome: {self.nome}\nNascimento: {self.nasc}\nGênero: {self.genero}\n"
                f"Idade: {self.calcIdade()} anos\nPeso: {self.peso} kg\nAltura: {self.altura} m\n"
                f"Classificação IMC: {target}\n")
