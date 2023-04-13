# Desenvolva um algoritmo em Python para determinar o Índice de Massa Corporal (IMC) de uma pessoa.
import time
from time import sleep
from tqdm import tqdm

print('\33[1:94m<---------ÍNDICE DE MASSA CORPORAL👩🏻‍⚕️🩺------------>\33[m\n')

print('\33[1:99m<---------INICIANDO SISTEMA------------>\33[m')
for i in tqdm(range(10)):
    time.sleep(0.1)

# Variável de controle
opc = True

# time.sleep(1)
while opc:
    # Criando as variáveis
    peso = float(input('\nDigite seu peso em (Kg): '))
    altura = float(input('Digite sua altura em (M): '))
    time.sleep(0.2)

    print('\n\33[1;99mPROCESSANDO SUAS INFORMAÇÕES 👀🔎.....\33[m')
    time.sleep(0.2)

    for i in tqdm(range(10)):
        time.sleep(0.2)

    # Realizando o cálculo de imc: Dividindo o peso em (Kg) pela altura ao quadrado (em metros)
    imc = (peso / altura ** 2)

    # Impressão do IMC
    print('\n\33[1;99mSeu IMC é: \33[m{:.4f}\n'.format(imc))

    # Determinando os indices utilizando uma estrutura condicional
    if imc < 18.5:
        print('\33[1;31mAbaixo do peso\33[m')
    elif imc >= 18.5 and imc <= 24.9:
        print('\33[1;32mNormal\33[m')
    elif imc >= 25 and imc <= 29.9:
        print('\33[1;31mSobrepeso\33[m')
    elif imc >= 30 and imc <= 39.9:
        print('\33[1;31mObesidade\33[m')
    else:
        print('\33[1;31mObesidade grave\33[m')

    # Time para simular a pergunta
    time.sleep(1)

    # Perguntando se o usuário deseja continuar
    resposta_usu = input('\n\33[1;99mDeseja continuar? \33[1;31m(S/N) \33[m').lower()

    # Verificando a resposta do usuario
    if resposta_usu != 's':
        opc = False

print('\n\33[1;99m...Saindo do sistema...\33[m')
time.sleep(0.1)
for i in tqdm(range(10)):
    time.sleep(0.1)
