import random
import string
from unicodedata import normalize
from colorama import Fore, Style

print('\n')
print(r'░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░███████╗  ███████╗░█████╗░██████╗░░█████╗░░█████╗░')
print(r'░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗')
print(r'░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║█████╗░░  █████╗░░██║░░██║██████╔╝██║░░╚═╝███████║')
print(r'██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██╔══╝░░  ██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══██║')
print(r'╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝███████╗  ██║░░░░░╚█████╔╝██║░░██║╚█████╔╝██║░░██║')
print(r'░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░╚══════╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝')

input('\nAperte ENTER para continuar... ')

print('\n')

escolha = int(input('Temas disponíveis: \n\n1 - INSTRUMENTOS MUSICAIS\n2 - FLORES\n3 - CORES\n\nEscolha o tema desejado: '))

if escolha == 1: 

    print('\nO tema que você escolheu é...\n')

    print(r'       ________________________      ')
    print(r'     /           ___ ___        \    ')
    print(r'     |\ .-------|:::/:::|--------;   ')
    print(r'     | |        |:::|:::|        |   ')
    print(r'     |\|_  ___ _|:::/:::| __ ____|   ')
    print(r'     | \  __  ___""" """_ ____ __`\  ')
    print(r'     | |\##\\###\\##\\###\\##\\### \                INSTRUMENTOS')
    print(r'     \ \ \\\\\\\\\\\\\\\\\\\\\\\\\\ \                 MUSICAIS')
    print(r'     |\ \||||||||||||||||||||||||||_|')
    print(r'     | | ;"""""""""""""""""""""""";"|')
    print(r'     | | |"""""".----------.""""""| |')
    print(r'     | | |     |\           \  |  | |')
    print(r'     | | |-----|\\___________\-|  | |')
    print(r'     | | |     | |---------- |  \ | |')
    print(r'     `\| |     | |         | |   `| |')
    print(r'       \_|       |           |    `\|')

    input('\n\nAperte ENTER para continuar... ')

    palavras = ['acordeon', 'alaúde', 'atabaque', 'baixo', 'balalaica', 'banjo', 'bateria', 'berimbau', 'bombo', 'carrilhão', 'castanhola', 'cavaquinho', 'celesta', 'chocalho', 'clarinete', 'clavicórdio', 'contrabaixo', 'corneta', 'cuíca', 'címbalo', 'cítara', 'fagote', 'flauta', 'flautim', 'gaita', 'gongo', 'guitarra', 'harmônica', 'harpa', 'lira', 'mandolim', 'maraca', 'oboé', 'ocarina', 'pandeiro', 'piano', 'prato', 'pífaro', 'rabeca', 'realejo', 'sanfona', 'serrote', 'sousafone', 'surdo', 'tambor', 'tamborim', 'tantan', 'teclado', 'triângulo', 'trombeta', 'trombone', 'trompa', 'trompete', 'tuba', 'tímpano', 'viola', 'violino', 'violoncelo', 'violão', 'xilofone', 'zabumba']

elif escolha == 2:

    print('\nO tema que você escolheu é...\n')

    print(r'                    ..ooo.')
    print(r'                 .888888888.')
    print(r'                 88"P""T"T888 8o')
    print(r'            o8o 8.8"8 88o."8o 8o')
    print(r'            88 . o88o8 8 88."8 88P"o')
    print(r'           88 o8 88 oo.8 888 8 888 88')
    print(r'           88 88 88o888" 88"  o888 88')
    print(r'           88."8o."T88P.88". 88888 88 ')
    print(r'           888."888."88P".o8 8888 888')
    print(r'           "888o"8888oo8888 o888 o8P"')
    print(r'            "8888.""888P"P.888".88P')
    print(r'             "88888ooo  888P".o888')
    print(r'               ""8P"".oooooo8888P')
    print(r'      .oo888ooo.    88NICK888P8')
    print(r'    o88888"888"88o.  "8888"".88   .oo888oo..                          FLORES')
    print(r'     8888" "88 88888.       88".o88888888"888.')
    print(r'     "8888o.""o 88"88o.    o8".888"888"88 "88P')
    print(r'      T888C.oo. "8."8"8   o8"o888 o88" ".=888"')
    print(r'       88888888o "8 8 8  .8 .8"88 8"".o888o8P')
    print(r'        "8888C.o8o  8 8  8" 8 o" ...o"""8888')
    print(r'          "88888888 " 8 .8  8   88888888888"')
    print(r'            "8888888o  .8o=" o8o..o(8oo88"')
    print(r'                "888" 88"    888888888""')
    print(r'                    o8P       "888"""')
    print(r'              ...oo88')
    print(r'     "8oo...oo888""')
    print(r'       ""888""')

    input('\n\nAperte ENTER para continuar... ')

    palavras = ['acácia', 'agapanto', 'alfazema', 'amarílis', 'anêmona', 'angélica', 'antúrio', 'astromélia', 'azaléia', 'begônia', 'bromélia', 'buganvílea', 'calêndula', 'camélia', 'cosmos', 'crisântemo', 'cravo', 'dália', 'dedaleira', 'edelvais', 'gardênia', 'gerânio', 'gerbena', 'girassol', 'gladíolo', 'glicínia', 'helicônia', 'hibisco', 'hidrângea', 'hortênsia', 'ipê', 'íris', 'ixora', 'jacinto', 'jasmim', 'jonquil', 'lavanda', 'lírio', 'lótus', 'madressilva', 'magnólia', 'malva', 'margarida', 'mimosa', 'miosótis', 'mosquitinho', 'narciso', 'ninféia', 'orquídea', 'papoula', 'passiflora', 'peônia', 'perpétua', 'petúnia', 'prímula', 'poinsétia', 'prímula', 'ranúnculo', 'rododendro', 'rosa', 'sálvia', 'tulipa', 'verbena', 'violeta', 'zínia']

else:

    print('\nO tema que você escolheu é...\n')

    print(f'{Fore.RED}████████████████████████████████████████████████████████████')
    print(f'{Fore.YELLOW}████████████████████████████████████████████████████████████')
    print(f'{Fore.GREEN}██████████████████████████CORES█████████████████████████████')
    print(f'{Fore.BLUE}████████████████████████████████████████████████████████████')
    print(f'{Fore.CYAN}████████████████████████████████████████████████████████████')
    print(f'{Style.RESET_ALL}\n')

    input('\n\nAperte ENTER para continuar... ')

    palavras = ['abóbora', 'açafrão', 'amarelo', 'âmbar', 'ameixa', 'amêndoa', 'ametista', 'anil', 'azul', 'bege', 'bordô', 'branco', 'bronze', 'cáqui', 'caramelo', 'carmesim', 'carmim', 'castanho', 'cereja', 'chocolate', 'ciano', 'cinza', 'cobre', 'coral', 'creme', 'damasco', 'dourado', 'escarlate', 'esmeralda', 'ferrugem', 'fúcsia', 'gelo', 'grená', 'gris', 'índigo', 'jade', 'jambo', 'laranja', 'lavanda', 'lilás', 'limão', 'magenta', 'malva', 'marfim', 'marrom', 'mostarda', 'negro', 'ocre', 'oliva', 'ouro', 'pêssego', 'prata', 'preto', 'púrpura', 'rosa', 'roxo', 'rubro', 'salmão', 'sépia', 'terracota', 'tijolo', 'turquesa', 'uva', 'verde', 'vermelho', 'vinho', 'violeta']

alfabeto = string.ascii_uppercase

def sorteio_palavra():
    palavra_sorteada = random.choice(palavras)
    for char in palavra_sorteada:
        if char not in alfabeto:
            palavra_sorteada = normalize('NFKD', palavra_sorteada).encode('ASCII', 'ignore').decode('ASCII')
    return palavra_sorteada.upper()

def forca(palavra_sorteada):
    palavra_incompleta = "_" * len(palavra_sorteada)
    letras_palavra = list(palavra_sorteada)
    letras_certas = []
    letras_usadas = []
    jogo_ganho = None
    palavra_oculta = ['_' for _ in range(len(palavra_sorteada))]

    tentativas = 6

    print(enforcado(tentativas))
    print(f'{palavra_incompleta}')
    
    while tentativas > 0 and '_' in palavra_incompleta:

        letra = ''
        
        while len(letra) != 1:
            letra = input('\nDigite uma letra: ').upper().encode('ASCII', 'ignore').decode('ASCII')
            if len(letra) != 1:
                print('Por favor digite uma letra.')

        if letra.isalpha():

            if letra in letras_usadas:
                print('\nVocê já usou esta letra. Escolha outra!')

            elif letra not in letras_palavra:
                print('\nVocê errou. Tente novamente!')
                tentativas -= 1
                letras_usadas.append(letra)
            
            else:
                print('\nVocê acertou! Continue assim!')
                letras_certas.append(letra)
                letras_usadas.append(letra)
                letras_palavra.remove(letra)
                palavra_oculta = list(palavra_incompleta)
                indices = [index for index, palpite in enumerate(palavra_sorteada) if letra == palpite]
                for i in indices:
                    palavra_oculta[i] = letra
                palavra_incompleta = ''.join(palavra_oculta)

        else:
            print('Seu palpite não é válido. Tente novamente!')

        print(enforcado(tentativas))
        print(palavra_incompleta)
        print(f'\nVocê já usou:', ' '.join(letras_usadas))
        print(f'\nVocê ainda tem {tentativas} chance(s)!')
        print('\n')

        if all(char != '_' for char in palavra_oculta):
            jogo_ganho = True
    
    if (jogo_ganho == True):
        print(f'{Fore.GREEN}Parabéns, você acertou a palavra!{Style.RESET_ALL}\n')

        print(f'{Fore.YELLOW}{Style.BRIGHT}             ___________ ')
        print(f"{Fore.YELLOW}{Style.BRIGHT}            '._==_==_=_.'")
        print(f'{Fore.YELLOW}{Style.BRIGHT}            .-\\:      /-.')
        print(f'{Fore.YELLOW}{Style.BRIGHT}           | (|:.     |) |')
        print(f"{Fore.YELLOW}{Style.BRIGHT}            '-|:.     |-'")
        print(f'{Fore.YELLOW}{Style.BRIGHT}              \\::.    /')
        print(f"{Fore.YELLOW}{Style.BRIGHT}               '::. .'")
        print(f'{Fore.YELLOW}{Style.BRIGHT}                 ) (')
        print(f'{Fore.YELLOW}{Style.BRIGHT}               _.\' \'.')
        print(f'{Fore.YELLOW}{Style.BRIGHT}              `"""""""`')
        print(f'{Style.RESET_ALL}\n')

    else:
        print(f'{Fore.RED}{Style.BRIGHT}Sinto muito, suas tentativas acabaram. A palavra era {palavra_sorteada}.{Style.RESET_ALL}\n\n')

        print(f'                                                                   -|-            ')
        print(f'                                                                    |             ')
        print(f"                                                                .-'~^~''-.        ")
        print(f"                                                              .'  _     _ `.      ")
        print(f'                                                              |  |_) | |_) |      ')
        print(f'                                                              |  | \ | |   |      ')
        print(f'                                                              |            |      ')
        print(f'                                                              |            |      ')
        print(f'{Fore.GREEN}{Style.BRIGHT}                                " -."-.\\"-."//.-".`-."_\\-.".-\\`=.........=`//-"')

        
        print(f'{Style.RESET_ALL}\n')

def enforcado(tentativas):
    
    estagios = [
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        """,

        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        """,

        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        """,

        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        """,

        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        """,

        """
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        """,

        """
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        """
    ]
    return estagios[tentativas]

palavra_sorteada = sorteio_palavra()

forca(palavra_sorteada)
