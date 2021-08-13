'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

from time import sleep

# Criando as variáveis nota

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Cálculo da média
media = ((n1+n2)/2)

# Temporizador
print('\n\33[1;91mCALCULANDO...\33[m')
sleep(0.75)

# Condicional para verificar a média do aluno e a situação
if media < 5:
    print('\nSua média foi de {}, você está REPROVADO!'.format(media))
elif media >= 5 and media < 7:
    print('\nSua média foi de {}, você está de RECUPERAÇÃO!'.format(media))
elif media > 7:
    print('\nSua média foi acima de {}, você está APROVADO!'.format(media))
