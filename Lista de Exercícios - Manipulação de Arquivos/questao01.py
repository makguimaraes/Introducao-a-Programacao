with open('frase.txt', 'w') as arquivo:

    arquivo.write(input('Digite a frase desejada: ') + '\n')

with open('frase.txt', 'r') as arquivo2:

    print(arquivo2.readlines())
