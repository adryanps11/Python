"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre
na tela sua porção inteira.

EX:
Digite um número : 6.127
o número 6.127 tem a parte inteira 6

"""
# Importando o math
import math

# Criando a variável num e solicitando ao usuário
num = float(input('Dgite um número: '))

# Utilizando o método math.trunc para eliminar os números após a vírgula
por = math.trunc(num)

# Impressão do resultado
print('O número digitado foi {} e a sua porção inteira foi: {}'.format(num, por))

