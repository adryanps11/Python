'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.'''

print('\n............TABUADA 2.0...........')


opc = 0
num = int(input('Digite um número para ver sua tabuada: '))
for c in range (1, 11):
    opc = c * num
    print('{} x {} = {}'.format(num, c, opc))
