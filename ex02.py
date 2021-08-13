#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivos
#e todas as informações possíveis sobre ela.

#Leia algo
leia = input('Digite algo: ')

#Determinando o tipo primitivo do valor digitado
print('O tipo primitivo desse valor é: {} '.format(leia),type(leia))

#Verifica se tem espaços, apresentado no valor digitado
print('Só tem Espaços? ',leia.isspace())

#Verifica se é um número
print('É um número? ',leia.isnumeric())

#Verifica se é um valor alfanumérico
print('É alfanumérico? ',leia.isalpha())

#Verifica se o valor digitado é maiúsculo
print('Éstá em maiúculo? ',leia.isupper())

#Verifica se o valor é minúsculo
print('Está em minúsculo? ',leia.islower())


