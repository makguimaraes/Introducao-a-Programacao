def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo += imposto
    return custo

taxaImposto = float(input('Digite a taxa sobre vendas: '))
custo = float(input('Digite o custo do item:'))

print(somaImposto(taxaImposto, custo))
