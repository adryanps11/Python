'''Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

print('<---------ALISTAMENTO MILITAR--------->')

# Módulo de data
from datetime import date

# Módulo para tempo
from time import sleep

# Pegando a data atual
atual = date.today().year

# Pedindo ao usuário para informar se é homen ou mulher
sexo = str(input('\nInforme seu sexo: ')).strip().lower()

# Temporizador
print('\n\33[1;93mPROCESSANDO SUAS INFORMAÇÕES....\33[m')
sleep(2)

# Verificando o sexo para fazer o alistamento
if sexo == 'masculino' or sexo == 'm':

    # Pedindo ao usuário para informar o ano de nascimento
    nasc = int(input('\nAno de Nascimento: '))

    # calculando a idade
    idade = atual - nasc

    # Temporizador novamente
    print('\n\33[1;93mAGUARDE...\33[m')
    sleep(2)

    # Mostrando na tela as informações para o usuário
    print('\nVocê nasceu em {}, tem {} anos, atualmente no ano de {}'.format(nasc, idade, atual))

     # Condicional para verificação
    if idade == 18:
        print('Você deve se ALISTAR IMEDIATAMENTE! ')
    elif idade < 18:
        #Variável para calcular se está no tempo para fazer o alistamento
        tempo = 18 - idade
        print('Ainda faltam {} anos para o seu alistamento'.format(tempo))
        # Variável ano para dizer em que ano será o alistamento
        ano = atual + tempo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        tempo = idade - 18
        print('Você deveria de ter se alistado há {} anos'.format(tempo))
        ano = atual - tempo
        print('Seu alistamento foi em {}'.format(ano))

elif sexo == 'feminino' or sexo == 'f':
    print('\nVocê não pode se alistar.')
else:
    print('\nDigite um sexo válido!')