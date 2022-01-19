r=' '
lista=list()
while True:
    n=(int(input('digite um numero')))


    if n in lista:
        print('numero duplicado nao adicionado...')
        r = str(input('quer continuar'))
    else:
        lista.append(n)
        print('numero adicionado com sucesso.')
        r=str(input('quer continuar'))

    if r == 'n':
        break
print(f'os numeros adicionados foram {sorted(lista)}')