''' Escreva um programa em Python que leia um número inteiro qualquer
 e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.'''

from time import sleep

print('<------CONVERSÃO DE BASE NUMÉRICA------>')

num = int(input('\nDigite um número inteiro: '))

print('''\nEscolha uma base para conversão:
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal
[ 4 ] - Todas Bases''')

opcao = int(input('\nSua opção: '))

print('\nPROCESSANDO.....')
sleep(2)

if opcao == 1:
    print('\nO número {} convertido para BINÁRIO é igual: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('\nO número {} convertido para OCTAL é igual: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('\nO número {} convertido para HEXADECIMAL é igual: {}'.format(num, hex(num)[2:]))
elif opcao == 4:
    print('O número {}\nBINÁRIO: {}\nOCTAL: {}\nHEXADECIMAL: {}'.format(num, bin(num)[2:], oct(num)[2:], hex(num)[2:]))
else:
    print('\nDigite uma opção válida!')
