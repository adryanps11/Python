"""Desenvolva um programa que pergunte a distância de uma viagemem km
- calcule o preço da passagem cobrando 0,50 por km para viagens de até 200 km
e 0,45 para viagens mais longas"""

print('-----------CUSTO DA VIAGEM-----------')

viagem = float(input('Informe a distância em KM que deseja viajar: '))

pas_1 = 0.50
pas_2 = 0.45

if viagem <= 200:
    print('O preço da viagem foi: R$ {:.2f}'.format(pas_1 * viagem))
else:
    print('O preço da viagem mais longa é R$ {:.2f}'.format(pas_2 * viagem))

