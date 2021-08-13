'''Crie um programa que faça o computador jogar Jokenpô com você.'''

print('==============JOKENPÔ================')

# Módulo para número randômico
from random import randint

# Módulo temporizador
from time import sleep

# Lista de itens
itens = ('Pedra', 'Papel', 'Tesoura')

# Computador recebe números aleatórios
computador = randint(0, 2)

# Impressão pedindo uma opção
print('''\nEscolha uma opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

# Pedindo o jogador para informar a jogada
jogador = int(input('\nDigite sua jogada: '))

# Temporizador do game
print('\n\33[1;93mJO', end='')
sleep(0.75)

print('KEN', end='')
sleep(0.75)

print('PÔ!!!\33[m\n')
sleep(0.75)

print('\33[1;97m-=-\33[m'*20)

# Recebendo as jogadas do computador e tanto do jogador
print('\nCOMPUTADOR = {}'.format(itens[computador]))
print('JOGADOR = {}\n'.format(itens[jogador]))

print('\33[1;97m-=-\33[m'*20)

'''
if computador == 0:  #computador jogou Pedra
    if jogador == 0:
        print('\nEMPATE!')
    elif jogador == 1:
        print('\nJOGADOR VENCEU!')
    elif jogador == 2:
        print('\nVOCÊ PERDEU!')
    else:
        print('\nOPÇÃO INVÁLIDA!')

elif computador == 1: #computador jogou Papel
    if jogador == 0:
        print('\nCOMPUTADOR VENCEU!')
    elif jogador == 1:
        print('\nEMPATE!')
    elif jogador == 2:
        print('\nVOCÊ VENCEU!')
    else:
        print('\nOPÇÃO INVÁLIDA!')

elif computador == 2: #computador jogou Tesoura
    if jogador == 0:
        print('\nVOCÊ VENCEU')
    elif jogador == 1:
        print('\nCOMPUTADOR VENCEU')
    elif jogador == 2:
        print('\nEMPATE')
    else:
        print('\nOPÇÃO INVÁLIDA!')


'''

# Pedra
if jogador == 0 and computador == 0:
    print('\nEMPATE!')
elif jogador == 0 and computador == 1:
    print('\nCOMPUTADOR VENCEU!')
elif jogador == 0 and computador == 2:
    print('\nJOGADOR VENCEU!')

# Papel
elif jogador == 1 and computador == 0:
    print('\nJOGADOR VENCEU!')
elif jogador == 1 and computador == 1:
    print('\nEMPATE!')
elif jogador == 1 and computador == 2:
    print('\nCOMPUTADOR VENCEU!')

# Tesoura
elif jogador == 2 and computador == 0:
    print('\nCOMPUTADOR VENCEU!')
elif jogador == 2 and computador == 1:
    print('\nJOGADOR VENCEU!')
elif jogador == 2 and computador == 2:
    print('\nEMPATE!')




