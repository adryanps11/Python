"""Faça um programa que leia uma frase pelo teclado e mostre
quantas vezes aparece a letra “A”, em que posição ela aparece
a primeira vez e em que posição ela aparece a última vez."""

# Criando a variável
frase = str(input('Digite uma frase: ')).upper().strip()

#Conta quantas vezes apareceu a letra "A"
print('A letra "A" apareceu {} vezes na frase'.format(frase.count('A')))

#Qual posição a primeira letra "A" apareceu
print('A primeira letra apareceu na posição: {}'.format(frase.find('A')+1))

#Qual posição ela aparece por ultimo
print('A letra "A" aparece por último na posição: {}'.format(frase.rfind('A')+1))
