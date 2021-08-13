#Desenvolva um algoritmo em Python para determinar o Índice de Massa Corporal (IMC) de uma pessoa.

print('\33[1:34m<---------ÍNDICE DE MASSA CORPORAL------------>\33[m\n')

from time import sleep

#Criando as variáveis
peso = float(input('Digite seu peso em (Kg): '))
altura = float(input('Digite sua altura em (M): '))

print('\n\33[1;93mPROCESSANDO SUAS INFORMAÇÕES.....\33[m\n')
sleep(2)

#Realizando o cálculo de imc: Dividindo o peso em (Kg) pela altura ao quadrado (em metros)
imc = (peso / altura**2)

#Impressão do IMC
print('\33[1;93mSeu IMC é: \33[m{:.4f}\n'.format(imc))

#Determinando os indices utilizando uma estrutura condicional
if imc < 18.5:
    print('\33[1;31mAbaixo do peso\33[m')
elif imc >= 18.5 and imc <= 24.9:
    print('\33[1;32mNormal\33[m')
elif imc >= 25 and imc <= 29.9:
    print('\33[1;31mSobrepeso\33[m')
elif imc >= 30 and imc <= 39.9:
    print('\33[1;31mObesidade\33[m')
else:
    print('\33[1;31mObesidade grave\33[m')



