def salarioPorHora(horas, valor_hora):
    if horas < 0 or valor_hora < 0:
        raise ValueError("Hora e valor devem ser >=0")
    return horas * valor_hora

if __name__ == "__main__":
    horas = float(input("Digite as horas trabalhadas no mês: "))
    valor_hora = float(input("Digite o valor por hora (R$): "))
    bruto = salarioPorHora(horas, valor_hora)
    print(f"Salário Bruto: R$ {bruto:.2f}")