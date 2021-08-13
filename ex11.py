# Faça um programa que leia a largura e a altura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta
# pinta uma área de 2m²

# Criando variáveis
lar = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))

# Calculando a área
area = (lar * alt)

# Calculando tinta necessária para pintar 2m²
tinta = (area/2)

# Impressão de da área e tinta necessária para pintar a parede
print('Sua parede tem dimensão de {} x {} e sua área é de {:.2f}m² \nPara pintar essa área será necessáriao: {:.2f}l de tinta.'.format(lar,alt,area,tinta))








