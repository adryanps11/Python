"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO"""

print('<--------ANO BISSEXTO--------->')

# Importando módulo
from datetime import date

# Pedindo para informar um ano ou digitar 0 para ver o ano atual
ano = int(input('Digite um ano ou informe 0 para ver o ano atual: '))

# Se o ano for igual a 0 informe o ano atual
if ano == 0:
   ano = date.today().year

# Verificando se é bissexto ou não
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} não é BISSEXTO'.format(ano))


