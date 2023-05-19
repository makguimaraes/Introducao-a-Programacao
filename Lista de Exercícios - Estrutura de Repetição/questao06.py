convidados = ['Wolfgang Amadeus Mozart', 'Oscar Wilde', 'Jane Austen', 'Alan Turing', 'Ada Lovelace']
qtd_convidados = len(convidados)

def escolha():
    opcao = input('O que deseja fazer?\n1 - Imprimir lista de convidados\n2 - Imprimir convites\n3 - Substituir convidado(s)\n4 - Sair\nDigite a opção desejada: ')
    while True:
        if opcao == '1':
            impressao_lista()
        elif opcao == '2':
            impressao_convites()
        elif opcao == '3':
            substituicao_convidado()
        elif opcao == '4':
            break
        else:
            print('Digite uma opção válida!')

def impressao_convites():
    for i in range(0, qtd_convidados):
        print(40*'-')
        print('CONVITE')
        print(40*'-')
        print(f'\n{convidados[i]}, você está convidado para um jantar na minha casa, no dia XX/XX às XX:00h.\n')
        print('ENDEREÇO: Rua das Avenidas, XXX\n\n')

def impressao_lista():
    print(40*'-')
    print(f'Código do Convidado = {i}')
    print(f'Nome do Convidado(a): {convidados[i]}')
    print(40*'-')
    print('\n')

def substituicao_convidado():
    convidado_faltoso = input('Digite o código do convidado faltoso: ')
    convidados[convidado_faltoso] = input('Digite o nome do novo convidado: ')
    outra_substituicao = input('Deseja substituir outro convidado? (S/N)')
    if outra_substituicao != 's' or 'S':
        escolha()

print(40*'-')
print('GERENCIADOR DE CONVITES')
print(40*'-')

escolha()
