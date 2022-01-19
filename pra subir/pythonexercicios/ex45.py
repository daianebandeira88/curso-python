from random import randint
from time import sleep
itens=('pedra','papel','tesoura')
computador=randint(0,2)
print('''suas opções:
[0] pedra:
[1] papel:
[2] tesoura:''')
jogador=int(input('qual é a sua jogada?'))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('põ!!')
print('-=' * 12)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence!')

    elif jogador == 2:
        print('computador vrnce!')
    else:
        print('opção invalida')
elif computador == 1:
    if jogador == 0:
        print('computador vence!')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence!')
    else:
        print('opção invalida')
elif computador == 2:
    if jogador == 0:
      print('jogador vence!')
    elif jogador == 1:
        print('computador vence!')
    elif jogador == 2:
        print('empate')
    else:
        print('opção invalida')


