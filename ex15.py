# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


#Criando as variáveis dias e km e solicitando para o cliente os dias alugados e km rodados.
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))

#Utilizamos as operações por dia e por km rodado
preco = (dias * 60) + (km * 0.15)

#Impressão do valor a pagar para alugar um carro
print('Total a pagar = R${:.2f}'.format(preco))


