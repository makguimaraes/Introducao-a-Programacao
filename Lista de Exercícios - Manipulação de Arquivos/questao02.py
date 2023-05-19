with open('frase.txt', 'r') as arquivo3:

    texto = arquivo3.read()

numero_chars = len(texto)

print(f'O arquivo contém {numero_chars} caracteres.')
