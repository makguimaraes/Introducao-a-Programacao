nome = input('Digite o nome do cliente: ')
numero_conta = input('Digite o número da conta: ')
saldo = float(input('Digite o saldo da conta: '))
debito = float(input('Digite o valor do débito: '))
credito = float(input('Digite o valor do crédito: '))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print('Saldo Positivo')
else:
    print('Saldo Negativo')
