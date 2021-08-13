'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

print('=========LOJA========')

preco = float(input('\nDigite o valor das compras R$: '))

print('''\nFORMAS DE PAGAMENTO 
        [ 1 ] à vista dinheiro/cheque
        [ 2 ] à vista no cartão
        [ 3 ] em até 2x no cartão
        [ 4 ] 3x ou mais no cartão
        ''')

opcao = int(input('Digite sua opção: '))

if opcao == 1:
    novo = preco - (preco * 10/100)
    print('\nSua compra à vista de R${} vai custar R${}'.format(preco, novo))

elif opcao == 2:
    novo = preco - (preco * 5/100)
    print('\nSua compra à vista no cartão de R${} vai custar R${}'.format(preco, novo))

elif opcao == 3:
    novo = preco
    parcelas = novo/2
    print('\nSua parcelada em 2x no cartão R${} vai custar R${}'.format(preco, parcelas))

elif opcao == 4:
    novo = preco + (preco * 20 / 100)
    qtd_parcelas = int(input('Quantas vezes deseja parcelar? '))
    parcelas = novo / qtd_parcelas
    print('\nSua compra parcela em {}x vai custar R${:.2f} com juros'.format(qtd_parcelas, parcelas))

else:
    print('\nOpção inválida')



