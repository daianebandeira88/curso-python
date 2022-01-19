somaidade=0
mediaidade=0
maioridadehomen=0
nomevelho=''
totmulher20=0
for p in range(1,5):
    print('-------{} pessoa-------'.format(p))
    nome=str(input('nome:')).strip()
    idade=int(input('idade'))
    sexo=str(input('sexo: [m/f]: ')).strip()
    somaidade+=idade
    if p ==1 and sexo in 'Mm':
        maioridadehomen=idade
        nomevelho=nome
    if sexo in 'Mn' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho= nome
    if sexo in 'Ff' and idade < 20:
        totmulher20+=1
        mediaidade=somaidade/4
print('a media de idade foi {}'.format(mediaidade))
print('o homen mais velho tem {} anos e se chama {}'.format(maioridadehomen,nomevelho))
print('ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
