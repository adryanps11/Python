""" Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo(sem coniderar espaços)
- Quantas letras tem o primeiro nome """

nome = str(input('Digite o seu nome completo: ')).strip()

#Nome completo em Maiusculo
print('Nome com letras maiusculas: {}'.format(nome.upper()))

#Nome completo em Minúsculo
print('Nome com letras minusculas: {}'.format(nome.lower()))

#Quantidade de caracteres sem espaços
print('O seu nome completo tem: {}'.format(len(nome) - nome.count(' ')))

#Quantidade de letras do primeiro nome

#print('O seu primeiro nome tem: {}'.format(nome.find(' ')))

dividir = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(dividir[0], len(dividir[0])))