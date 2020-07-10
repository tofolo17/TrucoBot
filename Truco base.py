import numpy as np
from numpy.random import default_rng
from termcolor import colored
# Made by Leo Neri


# Não otimizado
def jogar():
    rodadas1 = rodadas2 = 0
    while rodadas1 < 12 and rodadas2 < 12:
        print(f'Placar geral: {rodadas1} X {rodadas2}')
        print('\nNova rodada')
        if rodadas1 == 11 and rodadas2 == 11:
            print('\nMão de ferro!')
        vitorias1 = vitorias2 = 0
        numeros = {'4': 0, '5': 1, '6': 2, '7': 3, 'Dama': 4, 'Valete': 5, 'Rei': 6, 'Ás': 7, '2': 8, '3': 9}
        naipes = {'Ouros': 0, 'Espadas': 1, 'Copas': 2, 'Paus': 3}
        numerosinv = {v: k for k, v in numeros.items()}
        naipesinv = {v: k for k, v in naipes.items()}
        vira = np.random.randint(0, 10)
        if vira == 9:
            numeros[numerosinv[0]] = 10
        else:
            numeros[numerosinv[vira + 1]] = 10
        desempate = quemjoga = quempediu = 0
        rng = default_rng()
        meusnumeros = list(rng.choice(10, size=3))
        meusnaipes = list(rng.choice(4, size=3, replace=False))
        minhascartas = [0, 0, 0]
        trucado = 1
        while (vitorias1 < 2 and vitorias2 < 2) or (vitorias1 == 2 and vitorias2 == 2):
            print(f'\nRodada: {vitorias1} x {vitorias2}')
            print('Vira:', numerosinv[vira], '\n')
            print('Suas cartas:')
            for i in range(len(minhascartas)):
                minhascartas[i] = f'{numerosinv[meusnumeros[i]]} de {naipesinv[meusnaipes[i]]}'
                if rodadas1 == 11 and rodadas2 == 11:
                    print('{i}: XXXXXX'.format(i=i + 1))
                else:
                    print(f'{i+1}: ')
            if quempediu == 0:
                if trucado == 1:
                    print('\n0: Truco')
                if trucado == 6:
                    print('\n0: Pedir 9')
            else:
                if trucado == 3:
                    print('\n0: Pedir 6')
                if trucado == 9:
                    print('\n0:Pedir 12')
            print('9: Correr')
            numero2 = np.random.randint(0, 10)
            naipe2 = np.random.randint(0, 4)
            carta2 = str(list(numeros.values())[numero2]) + str(list(naipes.values())[naipe2])
            strcarta2 = str(list(numeros.keys())[numero2]) + ' de ' + str(list(naipes.keys())[naipe2])
            c2splitada = strcarta2.split()
            if numeros[c2splitada[0]] == 10:
                c2splitada[0] = 'Manilha'
            strcarta2 = ' '.join(c2splitada)
            if strcarta2.split()[0] == 'Manilha':
                if strcarta2.split()[2] == 'Paus':
                    strcarta2 = 'Zap'
                elif strcarta2.split()[2] == 'Copas':
                    strcarta2 = 'Copas'
                elif strcarta2.split()[2] == 'Espadas':
                    strcarta2 = 'Espadilha'
                else:
                    strcarta2 = 'Picafumo'
            bottrucado = np.random.randint(1, 11)
            quempediu = 0
            if bottrucado > 7 and rodadas2 != 11:
                quempediu = 1
                if trucado == 1:
                    print(colored('\nTRUCO', attrs=['bold']))
                    aceitatruco = input('Você aceita o truco?\nS ou N')
                    while aceitatruco.lower() != 's' and aceitatruco.lower() != 'n':
                        print('Responda S ou N!')
                        aceitatruco = input()
                    if aceitatruco.lower() == 's':
                        trucado = 3
                    else:
                        print('Jogador 1 correu!\n')
                        vitorias2 = 2
                        break
                if trucado == 6:
                    print(colored('\nNOVE\n', attrs=['bold']))
                    aceitatruco = input('Você aceita o nove?\nS ou N\n')
                    while aceitatruco.lower() != 's' and aceitatruco.lower() != 'n':
                        print('Responda S ou N!')
                        aceitatruco = input()
                    if aceitatruco.lower() == 's':
                        trucado = 9
                        continue
                    else:
                        print('Jogador 1 correu!\n')
                        vitorias2 = 2
                        break
            if quemjoga % 2 == 0:
                print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
            print('\nQual sua jogada?')
            print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
            print('Vira:', numerosinv[vira])
            for i in range(len(minhascartas)):
                minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                            naipe=naipesinv[meusnaipes[i]])
                if rodadas1 == 11 and rodadas2 == 11:
                    print('{i}: XXXXXX'.format(i=i + 1))
                else:
                    print('{i}: '.format(i=i + 1) + minhascartas[i])
            if quempediu == 0:
                if trucado == 1:
                    print('\n0: Truco')
                if trucado == 6:
                    print('\n0: Pedir 9')
            else:
                if trucado == 3:
                    print('\n0: Pedir 6')
                if trucado == 9:
                    print('\n0:Pedir 12')
            print('9: Correr')
            while True:
                try:
                    escolha = int(input())
                    while (int(escolha) not in list(range(1, len(minhascartas) + 1))) and (int(escolha) != 0) and (
                            int(escolha) != 9):
                        print('\nDigite um número válido!\n')
                        for i in range(len(minhascartas)):
                            minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                        naipe=naipesinv[meusnaipes[i]])
                            if rodadas1 == 11 and rodadas2 == 11:
                                print('{i}: XXXXXX'.format(i=i + 1))
                            else:
                                print('{i}: '.format(i=i + 1) + minhascartas[i])
                        if quempediu == 0:
                            if trucado == 1:
                                print('\n0: Truco')
                            if trucado == 6:
                                print('\n0: Pedir 9')
                        else:
                            if trucado == 3:
                                print('\n0: Pedir 6')
                            if trucado == 9:
                                print('\n0: Pedir 12')
                        print('9: Correr')
                        if quemjoga % 2 == 0:
                            print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
                        print('\nQual sua jogada?')
                        print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                        print('Vira:', numerosinv[vira])
                        escolha = int(input())
                    break
                except:
                    print('\nDigite um número!\n')
                    for i in range(len(minhascartas)):
                        minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                    naipe=naipesinv[meusnaipes[i]])
                        if rodadas1 == 11 and rodadas2 == 11:
                            print('{i}: XXXXXX'.format(i=i + 1))
                        else:
                            print('{i}: '.format(i=i + 1) + minhascartas[i])
                    if quempediu == 0:
                        if trucado == 1:
                            print('\n0: Truco')
                        if trucado == 6:
                            print('\n0: Pedir 9')
                    else:
                        if trucado == 3:
                            print('\n0: Pedir 6')
                        if trucado == 9:
                            print('\n0: Pedir 12')
                    print('9: Correr')
                    if quemjoga % 2 == 0:
                        print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
                    print('\nQual sua jogada?')
                    print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                    print('Vira:', numerosinv[vira])
            if escolha == 0 and quempediu == 0:
                if rodadas1 == 11:
                    print('Você perdeu o jogo! Não peça truco na mão de 11!')
                    rodadas2 = 12
                    break
                elif trucado == 1:
                    print(colored('\nTRUCO\n', attrs=['bold']))
                    chance3 = np.random.randint(1, 11)
                    if chance3 > 6:
                        print('Truco aceito!')
                        trucado = 3
                        chance6 = np.random.randint(1, 11)
                        if chance6 > 6:
                            print(colored('\nSEIS!\n', attrs=['bold']))
                            aceita6 = input('Você aceita o 6?\nS ou N\n')
                            while aceita6.lower() != 's' and aceita6.lower() != 'n':
                                print('Responda S ou N!')
                                aceita6 = input()
                            if aceita6.lower() == 's':
                                trucado = 6
                                continue
                            else:
                                print('Jogador 1 correu!\n')
                                vitorias2 = 2
                                break
                        print('\nQual sua jogada?')
                        print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                        print('Vira:', numerosinv[vira])
                        for i in range(len(minhascartas)):
                            minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                        naipe=naipesinv[meusnaipes[i]])
                            if rodadas1 == 11 and rodadas2 == 11:
                                print('{i}: XXXXXX'.format(i=i + 1))
                            else:
                                print('{i}: '.format(i=i + 1) + minhascartas[i])
                        if quempediu == 0:
                            if trucado == 1:
                                print('\n0: Truco')
                            if trucado == 6:
                                print('\n0: Pedir 9')
                        else:
                            if trucado == 3:
                                print('\n0: Pedir 6')
                            if trucado == 9:
                                print('\n0: Pedir 12')
                    else:
                        print('Jogador 2 correu!\n')
                        vitorias1 = 2
                        break
                elif trucado == 6:
                    print(colored('\nNOVE\n', attrs=['bold']))
                    chance9 = np.random.randint(1, 11)
                    if chance9 > 6:
                        print('Nove aceito!')
                        trucado = 9
                        chance12 = np.random.randint(1, 11)
                        if chance12 > 6:
                            print(colored('\nDOZE\n', attrs=['bold']))
                            aceita12 = input('Você aceita o 12?\nS ou N\n')
                            while aceita12.lower() != 's' and aceita6.lower() != 'n':
                                print('Responda S ou N!')
                            if aceita12.lower() == 's':
                                trucado = 12
                            else:
                                print('Jogador 1 correu!\n')
                                vitorias2 = 2
                                break
                        print('\nQual sua jogada?')
                        print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                        print('Vira:', numerosinv[vira])
                        for i in range(len(minhascartas)):
                            minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                        naipe=naipesinv[meusnaipes[i]])
                            if rodadas1 == 11 and rodadas2 == 11:
                                print('{i}: XXXXXX'.format(i=i + 1))
                            else:
                                print('{i}: '.format(i=i + 1) + minhascartas[i])
                        if quempediu == 0:
                            if trucado == 1:
                                print('\n0: Truco')
                            if trucado == 6:
                                print('\n0: Pedir 9')
                        else:
                            if trucado == 3:
                                print('\n0: Pedir 6')
                            if trucado == 9:
                                print('\n0: Pedir 12')
                        print('9: Correr')
                    else:
                        print('Jogador 2 correu!\n')
                        vitorias1 = 2
                        break
                while True:
                    try:
                        escolha = int(input())
                        while int(escolha) not in list(range(1, len(minhascartas) + 1)):
                            print('\nDigite um número válido!\n')
                            for i in range(len(minhascartas)):
                                minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                            naipe=naipesinv[meusnaipes[i]])
                                if rodadas1 == 11 and rodadas2 == 11:
                                    print('{i}: XXXXXX'.format(i=i + 1))
                                else:
                                    print('{i}: '.format(i=i + 1) + minhascartas[i])
                            if quempediu == 0:
                                if trucado == 1:
                                    print('\n0: Truco')
                                if trucado == 6:
                                    print('\n0: Pedir 9')
                            else:
                                if trucado == 3:
                                    print('\n0: Pedir 6')
                                if trucado == 9:
                                    print('\n0: Pedir 12')
                            print('9: Correr')
                            if quemjoga % 2 == 0:
                                print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
                            print('\nQual sua jogada?')
                            print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                            print('Vira:', numerosinv[vira])
                            escolha = int(input())
                        break
                    except:
                        print('\nDigite um número!\n')
                        for i in range(len(minhascartas)):
                            minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                        naipe=naipesinv[meusnaipes[i]])
                            if rodadas1 == 11 and rodadas2 == 11:
                                print('{i}: XXXXXX'.format(i=i + 1))
                            else:
                                print('{i}: '.format(i=i + 1) + minhascartas[i])
                        if quempediu == 0:
                            if trucado == 1:
                                print('\n0: Truco')
                            if trucado == 6:
                                print('\n0: Pedir 9')
                        else:
                            if trucado == 3:
                                print('\n0: Pedir 6')
                            if trucado == 9:
                                print('\n0: Pedir 12')
                        print('9: Correr')
                        if quemjoga % 2 == 0:
                            print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
                        print('\nQual sua jogada?')
                        print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                        print('Vira:', numerosinv[vira])
                        escolha = int(input())
            elif escolha == 9:
                print('Jogador 1 correu!\n')
                vitorias2 = 2
                break
            elif escolha == 0 and quempediu == 1:
                if trucado == 3:
                    print(colored('\nSEIS\n', attrs=['bold']))
                    botaceita6 = np.random.randint(1, 11)
                    if botaceita6 > 4:
                        print('6 aceito!')
                        trucado = 6
                        print('\nQual sua jogada?')
                        print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                        print('Vira:', numerosinv[vira])
                        while True:
                            try:
                                for i in range(len(minhascartas)):
                                    minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                                naipe=naipesinv[meusnaipes[i]])
                                    if rodadas1 == 11 and rodadas2 == 11:
                                        print('{i}: XXXXXX'.format(i=i + 1))
                                    else:
                                        print('{i}: '.format(i=i + 1) + minhascartas[i])
                                if quempediu == 0:
                                    if trucado == 1:
                                        print('\n0: Truco')
                                    if trucado == 6:
                                        print('\n0: Pedir 9')
                                else:
                                    if trucado == 3:
                                        print('\n0: Pedir 6')
                                    if trucado == 9:
                                        print('\n0: Pedir 12')
                                print('9: Correr')
                                escolha = int(input())
                                while (int(escolha) not in list(range(1, len(minhascartas) + 1))) and (
                                        int(escolha) != 0) and (int(escolha) != 9):
                                    print('\nDigite um número válido!\n')
                                    for i in range(len(minhascartas)):
                                        minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                                    naipe=naipesinv[meusnaipes[i]])
                                        if rodadas1 == 11 and rodadas2 == 11:
                                            print('{i}: XXXXXX'.format(i=i + 1))
                                        else:
                                            print('{i}: '.format(i=i + 1) + minhascartas[i])
                                    if quempediu == 0:
                                        if trucado == 1:
                                            print('\n0: Truco')
                                        if trucado == 6:
                                            print('\n0: Pedir 9')
                                    else:
                                        if trucado == 3:
                                            print('\n0: Pedir 6')
                                        if trucado == 9:
                                            print('\n0: Pedir 12')
                                    print('9: Correr')
                                    if quemjoga % 2 == 0:
                                        print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
                                    print('\nQual sua jogada?')
                                    print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                                    print('Vira:', numerosinv[vira])
                                    escolha = int(input())
                                break
                            except:
                                print('\nDigite um número!\n')
                                for i in range(len(minhascartas)):
                                    minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                                naipe=naipesinv[meusnaipes[i]])
                                    if rodadas1 == 11 and rodadas2 == 11:
                                        print('{i}: XXXXXX'.format(i=i + 1))
                                    else:
                                        print('{i}: '.format(i=i + 1) + minhascartas[i])
                                if quempediu == 0:
                                    if trucado == 1:
                                        print('\n0: Truco')
                                    if trucado == 6:
                                        print('\n0: Pedir 9')
                                else:
                                    if trucado == 3:
                                        print('\n0: Pedir 6')
                                    if trucado == 9:
                                        print('\n0: Pedir 12')
                                print('9: Correr')
                                if quemjoga % 2 == 0:
                                    print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
                                print('\nQual sua jogada?')
                                print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                                print('Vira:', numerosinv[vira])
                    else:
                        print('Jogador 2 correu!\n')
                        vitorias1 = 2
                        break
                elif trucado == 9:
                    print(colored('\nDOZE\n', attrs=['bold']))
                    botaceita12 = np.random.randint(1, 11)
                    if botaceita12 > 4:
                        print('12 aceito!')
                        print('\nQual sua jogada?')
                        print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                        print('Vira:', numerosinv[vira])
                        trucado = 9
                        while True:
                            try:
                                for i in range(len(minhascartas)):
                                    minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                                naipe=naipesinv[meusnaipes[i]])
                                    if rodadas1 == 11 and rodadas2 == 11:
                                        print('{i}: XXXXXX'.format(i=i + 1))
                                    else:
                                        print('{i}: '.format(i=i + 1) + minhascartas[i])
                                if quempediu == 0:
                                    if trucado == 1:
                                        print('\n0: Truco')
                                    if trucado == 6:
                                        print('\n0: Pedir 9')
                                else:
                                    if trucado == 3:
                                        print('\n0: Pedir 6')
                                    if trucado == 9:
                                        print('\n0: Pedir 12')
                                print('9: Correr')
                                escolha = int(input())
                                while (int(escolha) not in list(range(1, len(minhascartas) + 1))) and (
                                        int(escolha) != 0) and (int(escolha) != 9):
                                    print('\nDigite um número válido!\n')
                                    for i in range(len(minhascartas)):
                                        minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                                    naipe=naipesinv[meusnaipes[i]])
                                        if rodadas1 == 11 and rodadas2 == 11:
                                            print('{i}: XXXXXX'.format(i=i + 1))
                                        else:
                                            print('{i}: '.format(i=i + 1) + minhascartas[i])
                                    if quempediu == 0:
                                        if trucado == 1:
                                            print('\n0: Truco')
                                        if trucado == 6:
                                            print('\n0: Pedir 9')
                                    else:
                                        if trucado == 3:
                                            print('\n0: Pedir 6')
                                        if trucado == 9:
                                            print('\n0: Pedir 12')
                                    print('9: Correr')
                                    if quemjoga % 2 == 0:
                                        print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
                                    print('\nQual sua jogada?')
                                    print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                                    print('Vira:', numerosinv[vira])
                                    escolha = int(input())
                                break
                            except:
                                print('\nDigite um número!\n')
                                for i in range(len(minhascartas)):
                                    minhascartas[i] = '{num} de {naipe}'.format(num=numerosinv[meusnumeros[i]],
                                                                                naipe=naipesinv[meusnaipes[i]])
                                    if rodadas1 == 11 and rodadas2 == 11:
                                        print('{i}: XXXXXX'.format(i=i + 1))
                                    else:
                                        print('{i}: '.format(i=i + 1) + minhascartas[i])
                                if quempediu == 0:
                                    if trucado == 1:
                                        print('\n0: Truco')
                                    if trucado == 6:
                                        print('\n0: Pedir 9')
                                    else:
                                        if trucado == 3:
                                            print('\n0: Pedir 6')
                                        if trucado == 9:
                                            print('\n0: Pedir 12')
                                print('9: Correr')
                                if quemjoga % 2 == 0:
                                    print('\nJogador 2 jogou {c2}'.format(c2=strcarta2.split()[0]))
                                print('\nQual sua jogada?')
                                print('\nRodada: {v1} x {v2}'.format(v1=vitorias1, v2=vitorias2))
                                print('Vira:', numerosinv[vira])
                    else:
                        print('Jogador 2 correu!\n')
                        vitorias1 = 2
                        break
            carta1 = str(numeros[minhascartas[escolha - 1].split()[0]]) + str(
                numeros[minhascartas[escolha - 1].split()[0]])
            while carta2 == carta1:
                numero2 = np.random.randint(0, 10)
                carta2 = str(list(numeros.values())[numero2]) + str(list(naipes.values())[naipe2])
            mcsplitada = minhascartas[escolha - 1].split()
            if numeros[mcsplitada[0]] == 10:
                mcsplitada[0] = 'Manilha'
            strcarta1 = ' '.join(mcsplitada)
            vencedor = ''
            if strcarta1.split()[0] == 'Manilha':
                if strcarta1.split()[2] == 'Paus':
                    strcarta1 = 'Zap'
                elif strcarta1.split()[2] == 'Copas':
                    strcarta1 = 'Copas'
                elif strcarta1.split()[2] == 'Espadas':
                    strcarta1 = 'Espadilha'
                else:
                    strcarta1 = 'Picafumo'
            if int(carta1[:-1]) > int(carta2[:-1]):
                vencedor = 'Jogador 1'
                vitorias1 += 1
                print('\n{v} venceu jogando {c1} em cima de {c2}\n'.format(v=vencedor, c1=strcarta1, c2=strcarta2))
                if vitorias1 == 0 and vitorias2 == 0:
                    desempate = 1
            elif int(carta1[:-1] == 10) and int(carta2[:-1] == 10):
                if int(carta1) > int(carta2):
                    vencedor = 'Jogador 1'
                    vitorias1 += 1
                    print('\n{v} venceu jogando {c1} em cima de {c2}\n.'.format(v=vencedor, c1=strcarta1, c2=strcarta2))
                else:
                    vencedor = 'Jogador 2'
                    vitorias2 += 1
                    print('\n{v} venceu jogando {c2} em cima de {c1}\n.'.format(v=vencedor, c1=strcarta1, c2=strcarta2))
            elif int(carta1[:-1]) == int(carta2[:-1]):
                if vitorias1 == 1 and vitorias2 == 1:
                    if desempate != 0:
                        if desempate == 1:
                            print(colored('Jogador 1 venceu a rodada!\n\n', attrs=['bold']))
                            rodadas1 += trucado
                        else:
                            print(colored('Jogador 2 venceu a rodada!\n\n', attrs=['bold']))
                            rodadas2 += trucado
                else:
                    print('\nEmpate! Ambos jogaram {c1}!'.format(c1=strcarta2.split()[0]))
                vitorias1 += 1
                vitorias2 += 1
            else:
                vencedor = 'Jogador 2'
                vitorias2 += 1
                print('\n{v} venceu jogando {c2} em cima de {c1}.\n'.format(v=vencedor, c1=strcarta1, c2=strcarta2))
                if vitorias1 == 0 and vitorias2 == 0:
                    desempate = 2
            del minhascartas[escolha - 1]
            del meusnumeros[escolha - 1]
            del meusnaipes[escolha - 1]
            quemjoga += 1
        if vitorias1 >= 2 and vitorias2 != 2:
            print(colored('Jogador 1 venceu a rodada!\n\n', attrs=['bold']))
            rodadas1 += trucado
        elif vitorias2 >= 2 and vitorias2 != 1:
            print(colored('Jogador 2 venceu a rodada!\n\n', attrs=['bold']))
            rodadas2 += trucado
        else:
            print(colored('Empate! Não houveram vencedores.\n\n', attrs=['bold']))
        trucado = 1
        print(colored('-' * 100, attrs=['bold']))
    if rodadas1 > rodadas2:
        print(colored('Jogador 1 venceu o jogo! por {r1} X {r2}'.format(r1=rodadas1, r2=rodadas2), attrs=['bold']))
    else:
        print(colored('Jogador 2 venceu o jogo! por {r2} X {r1}'.format(r2=rodadas2, r1=rodadas1), attrs=['bold']))
    print(colored('-' * 100, attrs=['bold']))


jogar()
