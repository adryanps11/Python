'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''


print('\33[32m<---------ANALISANDO TRIÂNGULOS 2.0---------->\33[m')

# Importação do módulo time
from time import sleep

# Interações com pyhton
print('\33[37m-=-\33[m'*20)

# Criando variáveis
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

# Simulação de processamento
print('\33[36mPROCESSANDO SUAS INFORMAÇÕES.....\33[m\n')
sleep(2)

# Verificando os segmentos para ver se pode ou não criar um triãngulo
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima \33[33mPODEM FORMAR\33[m um triângulo.', end = ' ')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima \33[31mNÃO PODEM\33[m formar um triãngulo')

