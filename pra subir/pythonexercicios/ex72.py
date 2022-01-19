
numeros=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
resp=int(input('digite um numero de 0 á 10 : '))
while resp not in (0,1,2,3,4,5,6,7,8,9,10):
    resp=int(input('tente novamnete , digite um numero de 0 á 10 :'))

print(f' numero escolhido foi {numeros[resp]}')