numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("Números digitados: ", end = '')
for numero in numeros:
    print(numero, end = ' ')
