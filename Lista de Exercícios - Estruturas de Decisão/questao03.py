qtd_macas = int(input('Quantas maçãs foram compradas? '))

if qtd_macas >= 12:
    print(f'A compra custou R${qtd_macas * 1.00} ')
else:
    print(f'A compra custou R${qtd_macas * 1.30} ')
