# Faça um algoritmo que leia o preço de um novo produto e mostre seu novo preço
# com 5% de desconto.

# Criando as variáveis
preco = float(input('Digite o preço da mercadoria: '))

# Calculando o desconto multiplicando o preço da mercadoria por 5% e dividindo por 100
desconto = (preco * 5 / 100)

# Recebendo na variável resultado o preço menos o desconto
res = (preco - desconto)

# Impressão de preço da mercadoria com o desconto aplicado
print('Preço da mercadoria é R${:.2f} \nDesconto de 5%: R${:.2f}'.format(preco, res))

