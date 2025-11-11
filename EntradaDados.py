def calcular_salario_liquido(salario_bruto, experiencia_anos):
    # Descontos fixos (INSS, IRRF, etc.)
    inss = salario_bruto * 0.10  # Exemplo: 10% de INSS
    irrf = salario_bruto * 0.075 # Exemplo: 7.5% de IRRF
    
    # Bônus por experiência
    if experiencia_anos > 5:
        bonus = salario_bruto * 0.05
    elif experiencia_anos > 2:
        bonus = salario_bruto * 0.02
    else:
        bonus = 0
    
    salario_liquido = salario_bruto - inss - irrf + bonus
    return salario_liquido

# Exemplo de uso
salario_bruto = float(input("Digite o salário bruto: R$ "))
cargo = input("Digite o cargo: ")
experiencia = int(input("Anos de experiência: "))

salario_final = calcular_salario_liquido(salario_bruto, cargo, experiencia)

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Salário Líquido: R$ {salario_final:.2f}")