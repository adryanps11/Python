'''Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

print('<--------AUMENTOS MÚLTIPLOS-------->')

# Pedindo o salário do funcionário
salario = float(input('Digite o salário atual: '))

# Verificando se o salário é menor do que 1250
if salario <= 1250:
    novo = salario + (salario * 15) / 100
else:
    novo = salario + (salario * 10) / 100

# Impressão do resultado do salário atual
print('O seu salário atual de R${:.2f} será de R${:.2f}'.format(salario, novo))
