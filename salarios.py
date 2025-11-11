def calcular_salario_liquido(cargo, experiencia_anos):
    # Salários base por cargo
    salarios_base = {
        "analista": 3500.00,
        "gerente": 6000.00,
        "desenvolvedor": 5000.00,
        "estagiario": 1200.00,
        "diretor": 10000.00
    }
    
    # Verifica se o cargo existe
    if cargo.lower() not in salarios_base:
        return "Cargo não encontrado!"
    
    salario_bruto = salarios_base[cargo.lower()]
    
    # Calcula bônus por experiência
    if experiencia_anos > 5:
        bonus = salario_bruto * 0.10
    elif experiencia_anos >= 2:
        bonus = salario_bruto * 0.05
    else:
        bonus = 0
    
    salario_com_bonus = salario_bruto + bonus
    
    # Calcula descontos (INSS e IRRF)
    inss = salario_com_bonus * 0.10  # 10% de INSS
    
    # IRRF (Imposto de Renda)
    if salario_com_bonus <= 2500:
        irrf = 0
    elif salario_com_bonus <= 5000:
        irrf = salario_com_bonus * 0.075  # 7.5%
    else:
        irrf = salario_com_bonus * 0.15  # 15%
    
    salario_liquido = salario_com_bonus - inss - irrf
    
    # Retorna os resultados
    return {
        "Cargo": cargo.capitalize(),
        "Salário Bruto": f"R$ {salario_bruto:.2f}",
        "Bônus por Experiência": f"R$ {bonus:.2f}",
        "Salário com Bônus": f"R$ {salario_com_bonus:.2f}",
        "Desconto INSS (10%)": f"R$ {inss:.2f}",
        "Desconto IRRF": f"R$ {irrf:.2f}",
        "Salário Líquido": f"R$ {salario_liquido:.2f}"
    }

# Exemplo de uso
cargo = input("Digite o cargo (Analista/Gerente/Desenvolvedor/Estagiario/Diretor): ")

experiencia = int(input("Anos de experiência: "))

resultado = calcular_salario_liquido(cargo, experiencia)

print("\n--- Folha de Pagamento ---")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")