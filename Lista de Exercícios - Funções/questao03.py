def inversor_numero(numero):
    cp_numero = len(numero)
    numero_invertido = []
    for i in range(cp_numero, 0, -1):
        numero_invertido.append(numero[i - 1])

    numero_inteiro = int(''.join(numero_invertido))
    return numero_inteiro

numero = input('Digite um número inteiro: ')
oremun = inversor_numero(numero)
print(f'O número invertido é {oremun}.')
