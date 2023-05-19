def alunos_aprovados(): 

    alunos = {}
    count = 0

    for i in range(10):
        nome = input('Digite o nome do aluno: ')
        nota1 = float(input(f'Digite a primeira nota de {nome}: '))
        nota2 = float(input(f'Digite a segunda nota de {nome}: '))
        media = (nota1 + nota2) / 2

        alunos[nome] = [nota1, nota2, media]

    for notas in alunos.values():
        if notas[2] >= 7:
            count += 1
        
    print(f'{count} alunos tiveram uma média maior ou igual a 7.')

alunos_aprovados()
