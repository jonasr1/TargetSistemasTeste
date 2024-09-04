import json
from dataclasses import dataclass
from typing import List


@dataclass
class Faturamento:
    dia: int
    valor: float


def calcular_faturamento_diario(dados_faturamemto: List[Faturamento]) -> dict:
    valores = [faturamento.valor for faturamento in dados_faturamemto if faturamento.valor > 0]
    if not valores:
        return {
            "menor_valor": None,
            "maior_valor": None,
            "dias_acima_media": 0
        }
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    return {
        "menor_valor": min(valores),
        "maior_valor": max(valores),
        "dias_acima_media": dias_acima_media
    }


# Carregar dados do JSON
with open('dados.json', 'r') as arquivo:
    dados_json = json.load(arquivo)

# Converter dados JSON para uma lista de objetos Faturamento
dados = [Faturamento(**item) for item in dados_json]

estatisticas = calcular_faturamento_diario(dados)
print(f"Menor valor de faturamento: {estatisticas['menor_valor']}")
print(f"Maior valor de faturamento: {estatisticas['maior_valor']}")
print(f"Número de dias com faturamento acima da média: {estatisticas['dias_acima_media']}")
