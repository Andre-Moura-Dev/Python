taxas_cambio = {
    "USD": {"BRL": 5.10, "EUR": 1.50, "JPY": 150.25},
    "BRL": {"USD": 0.20, "EUR": 0.18, "JPY": 29.50},
    "EUR": {"USD": 1.09, "BRL": 5.50, "JPY": 161.75},
    "JPY": {"USD": 0.0067, "BRL": 0.034, "EUR": 0.0062}
}

def converter_moedas(base, valor, destino):
    if base in taxas_cambio and destino in taxas_cambio[base]:
        taxa = taxas_cambio[base][destino]
        convertido = valor * taxa
        print(f"{valor: .2f} {base} equivale a {convertido: .2f} {destino}")
    else:
        print("Conversão não disponível para essas moedas.")
        
moeda_origem = input("Informe a moeda de origem (USD, BRL, EUR, JPY): ").upper()
moeda_destino = input("Informe a moeda de destino (USD, BRL, EUR, JPY)").upper()
quantia = float(input("Informe o valor para converter: "))

converter_moedas(quantia, moeda_origem, moeda_destino)        