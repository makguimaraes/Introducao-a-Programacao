def contador_char(frase):
    contador = len(frase)
    return contador
    
frase = input('Digite a frase desejada: ')

numero_char = contador_char(frase)

print(f'A frase digitada tem {numero_char} caracteres.')
