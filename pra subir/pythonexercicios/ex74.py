from random import choices , sample
tamanho=5
valores=range(0,10)

lista=sample(valores, tamanho)
print(f'os valores sorteados foram {lista}')
print(f'o menor valor foi :{min(lista)}')
print(f'o maior valor foi :{max(lista)}')
