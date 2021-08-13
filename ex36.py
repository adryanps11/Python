'''Desenvolva um programa para aprovar o empréstimo bancário para compra de uma casa.
 O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

 Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou
 então o empréstimo será negado.'''

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento: '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('\nPara pagar uma casa de R${:.2f} em {} anos'.format(casa,anos), end=' ')
print('a pretação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')


