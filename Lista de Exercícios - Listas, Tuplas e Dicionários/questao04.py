def idade_altura():
    
    alunos = [
        [11, 1.68],
        [14, 1.75],
        [12, 1.72],
        [17, 1.76],
        [13, 1.65],
        [15, 1.57],
        [16, 1.60],
        [10, 1.58],
        [16, 1.79],
        [13, 1.73],
        [15, 1.70],
        [11, 1.62],
        [14, 1.68],
        [12, 1.75],
        [17, 1.77],
        [10, 1.59],
        [16, 1.80],
        [11, 1.66],
        [14, 1.58],
        [12, 1.75],
        [15, 1.56],
        [13, 1.77],
        [15, 1.76],
        [10, 1.57],
        [11, 1.73],
        [14, 1.59],
        [13, 1.56],
        [16, 1.75],
        [17, 1.67],
        [12, 1.78]
    ]

    altura_total = 0
    count = 0

    for aluno in alunos:
        altura_total += aluno[1]

    media_altura = altura_total / len(alunos)

    for aluno in alunos:
        if aluno[0] > 13 and aluno[1] < media_altura:
            count += 1

    print(f'{count} alunos com mais de 13 anos possuem altura inferior à média de altura.')

idade_altura()
