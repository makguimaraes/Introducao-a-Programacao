with open('frase.txt', 'a+') as arquivo4:
	
     arquivo4.write(input('Digite a continuação da frase: '))

with open('frase.txt', 'r') as arquivo_leitura:

    conteudo = arquivo_leitura.read()

print(conteudo)
