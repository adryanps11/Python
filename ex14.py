# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

# Criando a variável e pedindo a temperatura
c = float(input('Informe a temperatura em graus Celsius: '))

# Usando a fórmula para converter C em F
f = c * (9/5) + 32;

# Impressão de dados
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F!'.format(c,f))
