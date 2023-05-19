genero = input('Qual seu gênero? (F/M) ')
altura = float(input('Qual sua altura? (em m) '))

if genero.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
elif genero.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
else:
    print('Resposta inválida. Por favor, tente novamente!')

print(f'Seu peso ideal é {peso_ideal}' )
