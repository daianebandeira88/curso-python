total=totmil=menor=cont=0
barato=' '
while True:
    produto=str(input('nome do produto:'))
    preco=float(input('preço do produto: R$'))
    cont+=1
    total+=preco
    if preco >= 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato=produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp=' '
    while resp not in 'SN':
        resp=str(input('quer continuar [S /N]?')).upper()
    if resp =='N':
        break
print('{:-^40}'.format('fim do programa'))
print(f'o total da compra fica R${total:10.2f}')
print(f'tem {totmil} produto que custam mais de R$1000 reais')
print(f'o produto mais barato foi {barato} q custa R${menor}')

