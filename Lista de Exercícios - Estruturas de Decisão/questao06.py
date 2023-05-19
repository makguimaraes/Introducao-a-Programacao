numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'{numero2}, {numero1} ')
elif numero2 > numero1:
     print(f'{numero1}, {numero2}')
else:
     print('Os dois números digitados são iguais.')
