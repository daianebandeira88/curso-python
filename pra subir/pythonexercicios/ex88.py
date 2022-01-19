from random import randint , sample
from time import sleep
lista=[]
jogo=[]
tamanho=6
valores=range(1,60)
print('='*40)
print('       joga na mega sena')
print('='*40)
r=int(input('qauntos jogos voce quer que eu sorteie :'))
for list in range(0,r):
    jogo=sample(valores , tamanho)
    lista.append(jogo[:])
    jogo.pop()

print('       jogos gerados')
for pos, lin in enumerate(lista):
     print(f'jogo {pos+1}:{lin}')
     sleep(1)
print('-'*10,'boa sorte','-'*10)
