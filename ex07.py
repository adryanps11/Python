#Desenvolva um programa que leia as notas de um aluno, calcule e mostre a sua média

#Criando as variáveis com float pois as notas podem ser quebradas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nota = (n1 + n2)
media = (nota / 2)

#Impressão do resultado
print('A nota do aluno foi: {} e a média das notas é: {:.2f}'.format(nota,media))