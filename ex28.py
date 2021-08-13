"""Escreva um programa que faça o computador pensar em um número inteiro entre
 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador.

- O programa deverá escrever na tela se o usuário venceu ou perdeu"""

# Métodos import e from
from random import randint
from time import sleep

# Computador irá pensar ou número randomico
computador = randint(0,5)

# Impressão na tela
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5...')
print('-=-' * 20)

# Pedindo ao usuário para jogar
jogador = int(input('Em que número eu pensei? '))

# Simulando o processamento
print('PROCESSANDO....\n')

# Temporizador de 2 seg
sleep(2)

# Condicional para verificar se o jogador acertou ou não
if jogador == computador:
    print('PARABÉNS! Você acertou')
elif jogador > 5:
    print('OPÇÂO INVÁLIDA! Digite um número entre 0 e 5')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))




