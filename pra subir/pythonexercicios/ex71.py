print('='*30)
print('{: ^30}'.format(' Banco BCV'))
print('='*30)
print('cedulas disponiveis : R$50 R$20 R$10 R$1')
v=int(input('qual valor a ser sacado?'))
total=v
ced=50
totalced=0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'total de {totalced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced= 10
        elif ced == 10:
            ced = 1
        totalced=0
        if total ==0:
                break


