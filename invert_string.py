def inverter_string(s: str) -> str:
    lista_chars = list(s)  # Converte a string em uma lista de caracteres
    tamanho = len(lista_chars)
    resultado_invertido = [''] * tamanho
    for i in range(tamanho):
        resultado_invertido[i] = lista_chars[tamanho - 1 - i]
    return ''.join(resultado_invertido)


entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
