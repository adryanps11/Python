''' A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

# Módulo para buscar o ano atual
from datetime import date

# Recebendo o ano atual na var
atual = date.today().year

# Variável criada para solicitar o ano de nascimento
nasc = int(input('Digite o ano de nascimento: '))

idade = atual - nasc

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM!')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL!')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR!')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR!')
else:
    print('Classificação: MASTER!')






