
lista=[]
dado=[]
while True :
    n=dado.append(input('nome:'))
    p=dado.append(int(input('peso:')))
    if len(lista) == 0:
        maior = menor =dado[1]
    else:
        if dado[1]> maior:
            maior = dado[1]
            if dado[1] < menor:
                menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    r=input('quer continuar S/N ?')
    if r =='n':
        break
print(lista)
print('='*45)
print(f'ao todo vc cadastrou {len(lista)} pessoas')

print(f'o maior peso foi de {maior}')
print(f' o menor peso foi {menor}')
