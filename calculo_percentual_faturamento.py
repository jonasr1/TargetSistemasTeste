faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


def calculo_percentual_faturamento(faturamento_estados: dict) -> dict:
    total = sum(faturamento_estados.values())
    return {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}


percentuais_estados = calculo_percentual_faturamento(faturamento)

for estado, valor in percentuais_estados.items():
    print(f"{estado}: {valor:.2f}%")
