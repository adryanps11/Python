"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR"""

print('<--------PAR ou ÍMPAR------------>')

# Pedindo um número
num = int(input('Digite um número: '))

# Quando o número solicitado for módulo de 2 igual a 0 ele será par
if num % 2 == 0:
    print('Número: {} PAR'.format(num))
else:
    print('Número: {} ÍMPAR'.format(num))
