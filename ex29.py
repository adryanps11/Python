"""
Escreva um programa que leia a velocidade de um carro.
- Se ele ultrapassar de 80 km/hr. Mostre uma mensagem dizendo que ele foi multado.
- A multa vai custar R$ 7.00 por cada km/h acima do limite
"""

print('<---------Radar ELetrônico---------->')

# Pedindo ao usuário para informar a velocidade do carro
vel = float(input('Informe a velocidade do carro: '))

# Operação velocidade menos 80km/h
multa = ((vel - 80) * 7)

# Verifica se a velocidade do carro for maior que 80 ele recebe o valor da multa a ser pago
if vel > 80:
    print('Você foi multado em R$ {} reais.'.format(multa))
else:
    print('Parabéns! Continue dirigindo com cuidado')