from random import randint
s=v=0
j=c=tipo=''

print('-='*20)
print(' vamos jogar PAR ou IMPAR')
print('-='*20)
while True:
    j=int(input('diga um numero'))
    c=randint(0,10)
    s=j+c
    while tipo not in 'P I':
        tipo = str(input('vc escolhe PAR ou IMPAR ? [P/I]')).strip().upper()
    print(f'voce jogou {j} e o computador {c} .total de {s}')
    if tipo =='P':
        if s % 2 ==0:
         print('voce venceu')
         v=+1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if s %2 ==1:
            v+=1
        else:
          print(' voce perdeu ')
          break
    print('vamos jogar novamente...')
print(f'GAME OVER !!voce venceu  {v} vezes')
