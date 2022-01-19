from datetime import date
atual=date.today().year
totmaior=0
totmenor=0
for c in range(1,8):
    d = int(input('digite ano de nascimenro da {} pessoa'.format(c)))
    idade=atual- d
    if idade >= 21:
       totmaior+=1
    else:
       totmenor+=1
print('ao todo tivemos {} de maior'.format(totmaior))
print('e {} pessoas de menor'.format(totmenor))
