r='s'
lista=list()
listapar=list()
listaimpar=list()
while r=='s':
    n=int(input('digite um valor'))
    lista.append(n)
    if r != 's' or 'n':
       r=input('quer continuar S/N')
    if r =='n':
        break
print(f'a lista completa é {lista}')
for n in lista:
 if n %2 ==0:
    listapar.append(n)
 else:
    listaimpar.append(n)
print(f'a lista com numeros pares é {listapar}')
print(f'a lista com numeros impar é {listaimpar}')
