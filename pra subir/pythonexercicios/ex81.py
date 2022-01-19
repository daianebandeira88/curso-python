r='s'
lista=list()
while r=='s':
    n=int(input('digite um valor'))
    lista.append(n)
    if r != 's' or 'n':
       r=input('quer continuar S/N')
    if r =='n':
        break
print(f'voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'os valores em ordem decrescente são {lista}')
if 5 in lista:
         print('o valor 5 faz parte da lista')
else:
         print('o valor 5 não foi encontrado na lista')


