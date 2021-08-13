""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triãngulo retãngulo, calcule e mostre o comprimento da hipotenusa """

# Importando módulo
from math import hypot

# Criando variáveis para pedir seus comprimentos
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

# Sem usar o math
#hi = (co ** 2 + ca ** 2) ** (1/2)

# Cria a variável hipotenusa e recebe o math.hypot
hi = hypot(co, ca)

# Impressão dos resultados
print('A hipotenusa irá medir: {:.2f}'.format(hi))
