'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

print('<---------COMPARANDO NÚMEROS--------->')

from time import sleep

num1 = int(input('\nInforme o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))

print('\nPROCESSANDO......')
sleep(2)

if num1 > num2:
    print('\nO PRIMEIRO valor é MAIOR que o segundo.')
elif num2 > num1:
    print('\nO SEGUNDO valor é MAIOR que o primeiro')
else:
    print('\nOs DOIS valores são IGUAIS.')
