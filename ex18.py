""" Faça um programa que leia um ãngulo qualquer e mostre na tela o valor de seno
coseno e tangente desse angulo """

# Importação do módulo
import math

# Solicitando para informar um ângulo
ang = float(input('Informe um ângulo qualquer: '))

# Variáveis recebendo os módulos math para fazer a operação matemática
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

# Impressão dos resultados dos angulos
print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tang))
