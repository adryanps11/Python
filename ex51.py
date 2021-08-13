'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

print('='*45)
print('           10 TERMOS DE UMA PA')
print('='*45)

primeiro = int(input('primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + 1, razao):
    print('{}'.format(c), end=' - ')
print('ACABOU')

