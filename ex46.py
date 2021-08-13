'''Faça um programa que mostre na tela uma contagem regressiva para o
estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

print('<---------------CONTAGEM REGRESSIVA--------------->')

# Módulo time
from time import sleep

print('Preparando lançamento dos Fogos de Artifício')
print('-=-'*20)
sleep(1)

# Laço de repetição
for c in range(10, -1, -1):
    print(c)
    sleep(0.5) # Temporizador
print('\nEXPLODIU!!!!!!')
