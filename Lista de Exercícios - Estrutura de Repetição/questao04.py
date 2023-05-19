numero = int(input('Digite o número cuja tabuada deseja ver: '))

for multiplicando in range(1,10):
    produto = numero * multiplicando
    print(f'{numero} * {multiplicando} = {produto}')
    multiplicando += 1
