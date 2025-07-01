# Exercício de Gerenciador de Pagamentos
print('-'*20, 'Lojas Valverde', '-'*20)
preco = float(input('Preço das compras: '))
formadepagamento = int(input('Forma de paga,mento:\n'
                             '1 - À vista dinheiro\n'
                             '2 - À vista cartão\n'
                             '3 - 2x cartão\n'
                             '4 - 3x ou mais cartão\n'
                             'Escolha uma opção: '))
if formadepagamento == 1:
    desconto = preco * 0.1  # 10% de desconto
    total = preco - desconto
    print(f'Você ganhou 10% de desconto!')
    print(f'O valor total a pagar é: R${total:.2f}')
elif formadepagamento == 2:
    desconto = preco * 0.05  # 5% de desconto
    total = preco - desconto
    print(f'Você ganhou 5% de desconto!')
    print(f'O valor total a pagar é: R${total:.2f}')
elif formadepagamento == 3:
    total = preco  # não tem desconto
    parcela = total / 2
    print(f'O valor total a pagar é: R${total:.2f}')
    print(f'Você pagará em 2x de R${parcela:.2f}')
elif formadepagamento == 4:
    juros = preco * 0.2  # 20% de juros
    total = preco + juros
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print(f'O valor total a pagar é: R${total:.2f}')
    print(f'Você pagará em {parcelas}x de R${parcela:.2f}')
