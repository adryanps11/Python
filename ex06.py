# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

# Entrada com um número
num = int(input('Digite um número: '))

# Impressão do número multiplicando pelo dobro e pelo triplo e no final descobrindo a raiz quadrada
print('O Dobro de {} vale = {} \n o triplo {} vale = {} \n e a Raiz quadrada de {} é igual {:.2f} '.format(num, (num * 2), num , (num * 3), num, pow(num , (1/2))))

# -- Modelo com utilização de variáveis -- #

# Declaração de variaveis
#num = int(input('Digite um número: '))
#d = num * 2
#t = num * 3
#r = num ** (1/2)

# Impressão com utilização de variaveis no método format
#print('O dobro de {} vale = {} \n o triplo de {} vale = {} \n e Raiz Quadrada de {} é igual = {:.2f}'.format(num, d, num, t, num, r))

