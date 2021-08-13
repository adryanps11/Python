# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento

# Criando variável
sal = float(input('Digite seu salário: '))

# Calculando o salário
aum = (sal * 15 / 100)

# Recebendo na variavel res o salário mais 15% de aumento
res = (sal + aum)

# Impressão do novo salário com 15% de aumento
print('Seu novo salário será: R${:.2f}'.format(res))

