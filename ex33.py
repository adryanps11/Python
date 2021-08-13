'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

print('<--------MAIOR E MENOR VALORES--------->')

# Solicitando três valores ao usuário

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

# Verificando quem é menor
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando quem é o maior
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Impressão de quem é maior e quem é menor
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))





