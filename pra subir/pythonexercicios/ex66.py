n=s=cont=0
while True:
    n=int(input('digite um numero (999 pra parar):'))

    if n == 999:
        break
    s+=n
    cont+=1
print(f'a soma dos {cont} valores é {s}' )