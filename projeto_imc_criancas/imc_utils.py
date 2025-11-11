from datetime import datetime

class DadosInvalidosError(Exception):
    """Exceção personalizada para dados inválidos."""
    pass

class Dados:
    def __init__(self, nome, nasc, genero, peso, altura):
        self.nome = nome
        self.nasc = nasc
        self.genero = genero
        self.peso = peso
        self.altura = altura
        self.idade = self._calcular_idade()

    def _calcular_idade(self):
        """Calcula a idade com base na data de nascimento."""
        try:
            data_nascimento = datetime.strptime(self.nasc, "%Y-%m-%d")
            return (datetime.now() - data_nascimento).days // 365
        except ValueError:
            raise DadosInvalidosError("Data de nascimento inválida. Use o formato YYYY-MM-DD.")

    def _calcular_imc(self):
        """Calcula o IMC com base no peso e altura."""
        return self.peso / (self.altura ** 2)

    def classificar_imc(self):
        """Retorna a classificação do IMC baseada na tabela etária e de gênero."""
        imc = self._calcular_imc()

        tabela = {
            'Masc': {
                6: [14.5, 16.7, 18],
                7: [15.0, 17.4, 19.1],
                8: [15.6, 16.8, 20.3]
            },
            'Femi': {
                6: [14.3, 16.2, 17.4],
                7: [14.9, 17.2, 18.9],
                8: [15.6, 18.2, 20.3]
            }
        }

        if self.genero not in tabela or self.idade not in tabela[self.genero]:
            raise DadosInvalidosError(f"Idade ({self.idade}) ou gênero ({self.genero}) inválido(s).")

        limites = tabela[self.genero][self.idade]

        if imc < limites[0]:
            return "Abaixo do peso"
        elif imc < limites[1]:
            return "Peso normal"
        elif imc < limites[2]:
            return "Sobrepeso"
        else:
            return "Obesidade"

    def __str__(self):
        try:
            classificacao = self.classificar_imc()
        except DadosInvalidosError as erro:
            classificacao = f"Erro: {erro}"

        return (
            f"Nome: {self.nome}\n"
            f"Nascimento: {self.nasc}\n"
            f"Gênero: {self.genero}\n"
            f"Idade: {self.idade} anos\n"
            f"Peso: {self.peso} kg\n"
            f"Altura: {self.altura} m\n"
            f"Classificação IMC: {classificacao}\n"
        )