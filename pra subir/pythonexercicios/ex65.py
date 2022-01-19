num = soma = med = tot=0

r='s'
while r =='s':
    num=int(input('digite um numero'))
    r=str(input('quer continuar S /N ?')).lower()
    soma+=num
    tot+=1
    med=soma/tot
    if tot == 1:
         maior=menor=num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('vc digitou {} numeros e a media entre eles é {} '.format(tot, med ))
print('o maior valor foi {} e o menor foi {} '.format(maior,menor))
if r == 'n':
    print('fim')