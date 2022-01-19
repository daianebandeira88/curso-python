f=str(input('escreva uma frase')).upper().strip()
print(' a frase tem a letra A {} vezes'.format(f.count('A')))
print('a primeira letra A apareceu na posição {}'.format(f.find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(f.rfind('A')+1))