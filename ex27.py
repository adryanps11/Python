"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente."""

# Variável string recebendo o strip para anular espaços indesejáveis
n = str(input('Digite seu nome completo: ')).strip()

# Variável nome recebe n para dividir
nome = n.split()

# Reconhecendo o primeiro nome na posição 0
print('O seu primeiro nome é: {}'.format(nome[0]))

# Reconhecendo o último nome com a opção len para ver o último nome
ul = nome[len(nome)-1]
print('o seu último nome é: {}'.format(ul))

