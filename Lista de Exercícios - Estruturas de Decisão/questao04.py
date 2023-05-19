nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média de {nome} foi {media}')

if media >= 6:
    print(f'{nome} passou de ano! ')
else:
    print(f'{nome} reprovou.')
