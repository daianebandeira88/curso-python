n1=n2=' '
index=0
lista=list()
for cont in range(0,5):
    lista.append(int(input('digite um numero')))
print(lista)
n1=max(lista)
n2=min(lista)
print(f'o MAIOR foi: {n1} e esta na posiçao {lista.index(n1)+1}')
print(f'o MENOR foi: {n2} e esta na posiçao { lista.index(n2)+1}')
print('fim')