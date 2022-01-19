pri=int(input('primeiro valor'))
seg=int(input('segundo valor'))
ter=int(input('terceiro valor'))
maior = pri
if (seg>maior):
    maior=seg
if (ter > maior):
    maior=ter
menor = pri
if (seg < menor):
    menor = seg
if (ter < menor):
    menor = ter
print('menor:' ,menor)
print('maior:',maior)