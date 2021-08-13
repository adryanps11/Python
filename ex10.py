# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar. Considerando US$ 1,00 = R$3.27

# Criação da variável
num = float(input('Digite o saldo em sua carteira: '))
dolar = 3.27

# Dividindo o número digitado pelo valor do dólar
res = float(num / dolar)

#Impressão do resultado da carteira e quantos dólares a pessoa poderá comprar.
print('Você possui em sua carteira: R$ {:.2f}, e dará para comprar US${:.2f} dólar'.format(num, res))
