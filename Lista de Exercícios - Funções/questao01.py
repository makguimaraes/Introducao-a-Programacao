def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo += imposto
    return custo

taxaImposto = float(input('Digite taxa'))
custo = float(input('Digite custo:'))

print(somaImposto(taxaImposto, custo))
