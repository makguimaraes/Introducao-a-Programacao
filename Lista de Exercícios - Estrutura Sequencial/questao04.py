salario_hora = float(input('Digite o valor que vc recebe por hora de trabalho: '))
horas_trabalhadas = float(input('Digite o número de horas que vc trabalhou no mês: '))

salario_total = salario_hora * horas_trabalhadas

print(f'O salário total do mês será de R${salario_total:.2f}')
