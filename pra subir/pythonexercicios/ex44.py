print('{:=^40}'.format(' lojas guanabara  '))
p=float(input(' preço do produto'))
print(p)
print('escolha a opção de pagamento')
pag=int(input('''[1] á vista com cheque/dinheiro;
[2] á vista no cartão;
[3] 2x no cartão;
[4] 3x ou mais no cartão;  '''))
print(pag)
if pag == 1:
    print('valor á pagar R$ {} com 10% de desconto'.format(p-(p*10)/100))
elif pag == 2:
    print('o valor a pagar é R$ {} com 5% de desconto'.format(p-(p*5/100)))
elif pag == 3:
    print('ovalor a ser pago é R$ {}'.format( p))
elif pag == 4:
    p=p+(p*20/100)
    totpar=int(input('quantas parcelas?'))
    parcela=p/totpar
    print('sua compra sera parcelada em {}x de R$ {}'.format(totpar,parcela))
    print('o valor final a ser pago é R$ {} com 20% de juros'.format(p))
else:
    pag >= 5
    print('opção invalida!')
